import pathlib
from ..utils.csvfile import read_dictionary, write_dictionary
from ..utils.tarfile import file_in_corpus, read_lines_from_tar_file

def coverage(corpus, tokens, tokenizer = None):
    """
    Calculates the Zif's law coverage of a given set of tokens on the corpus an a document by document basis

    Parameters
    ----------
    corpus : str
        The tarball containing the corpus
    tokens: str
        The file containing the list of tokens to get a % coverage on
    tokenizer: function
        Optional: function to take in a line (str) and output a list of tokens (str[])

    Example
    ---------
    import corpustools.measure as ctm; ctm.coverage('d:/working/corpus.tar', 'd:/working/tokens.csv')
    """

    corpus = pathlib.Path(corpus)

    measures_file = corpus.parent.joinpath('./coverage.csv')
    if measures_file.exists():
        measures_file.unlink()
    if tokenizer == None:
        tokenizer = lambda line: [token.upper() for token in line.strip().split() if len(token) > 0]

    tokens = set(read_dictionary(tokens).keys())
    measures = _measures(corpus, tokens, tokenizer)
    _write_measures(measures_file, measures)



def _measures(corpus, tokens, tokenizer):

    print('Measuring Coverage...')
    measures = {}
    
    for (tar_info, tar_file) in file_in_corpus(corpus):
        total_tokens = 0
        total_coverage = 0
        for line in read_lines_from_tar_file(tar_file):
            line_tokens = tokenizer(line)
            total_tokens = total_tokens + len(line_tokens)
            for token in line_tokens:
                if token in tokens:
                    total_coverage = total_coverage + 1
                    pass
                pass
            pass
        measures[tar_info.name] = round(total_coverage/total_tokens, 8)

    return measures

def _write_measures(file_name, measures):

    print('Writing Measures...')
    write_dictionary(file_name, measures)
