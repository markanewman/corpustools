import pathlib
from ..utils.csvfile import write_dictionary
from ..utils.tarfile import file_in_corpus, read_lines_from_tar_file
from statistics import mean

def TTR(corpus, tokenizer = None):
    """
    Calculates the Moving Average Type Token Ratio for each document in a given corpus

    Parameters
    ----------
    corpus : str
        The tarball containing the corpus
    tokenizer: function
        Optional: function to take in a line (str) and output a list of tokens (str[])

    Example
    ---------
    import corpustools.measure as ctm; ctm.TTR('d:/working/corpus.tar')
    """

    corpus = pathlib.Path(corpus)

    measures_file = corpus.parent.joinpath('./TTR.csv')
    if measures_file.exists():
        measures_file.unlink()
    if tokenizer == None:
        tokenizer = lambda line: [token.upper() for token in line.strip().split() if len(token) > 0]

    measures = _measure_corpus(corpus, tokenizer)
    _write_measures(measures_file, measures)

    return (measures_file, mean(measures.values()))

def _measure_corpus(corpus, tokenizer):

    print('Measuring TTR...')
    measures = {}

    for (tar_info, tar_file) in file_in_corpus(corpus):
        lines = read_lines_from_tar_file(tar_file)
        flat_list = [token for line in lines for token in tokenizer(line)]
        measures[tar_info.name] = _measure_document(flat_list)

    return measures

def _measure_document(tokens):
    l = len(tokens)
    if l == 0:
        ttr = 0
        pass
    else:
        ttr = len(set(tokens)) / l
        pass
    return round(ttr, 8)

def _write_measures(file_name, measures):

    print('Writing Measures...')
    write_dictionary(file_name, measures)
