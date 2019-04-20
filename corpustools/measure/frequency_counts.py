import pathlib
import progressbar as pb
from ..utils.csvfile import write_dictionary
from ..utils.tarfile import file_in_corpus, read_lines_from_tar_file

def frequency_counts(corpus, tokenizer = None):
    """
    Counts the unique tokens for the entire corpus

    Parameters
    ----------
    corpus : str
        The tarball containing the corpus
    tokenizer: function
        Optional: function to take in a line (str) and output a list of tokens (str[])

    Example
    ---------
    import corpustools.measure as ctm; ctm.frequency_counts('d:/working/corpus.tar')
    """

    corpus = pathlib.Path(corpus)

    measures_file = corpus.parent.joinpath('./counts.csv')
    if measures_file.exists():
        measures_file.unlink()
    if tokenizer == None:
        tokenizer = lambda line: [token.upper() for token in line.strip().split() if len(token) > 0]

    counts = _collect_counts(corpus, tokenizer)
    _write_measures(measures_file, counts)

def _collect_counts(corpus, tokenizer):

    print('Collecting Token Counts ...')
    counts = {}
    
    for (tar_info, tar_file) in file_in_corpus(corpus):                    
        for line in read_lines_from_tar_file(tar_file):
            for token in tokenizer(line):
                if token not in counts:
                    pass
                    counts[token] =  0
                counts[token] = counts[token] + 1
            pass
        pass        

    return counts

def _write_measures(file_name, measures):

    print('Writing Measures...')
    write_dictionary(file_name, measures, value_sort = True, asc_sort = False)
