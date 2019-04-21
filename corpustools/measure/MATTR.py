import pathlib
from ..utils.csvfile import write_dictionary
from ..utils.tarfile import file_in_corpus, read_lines_from_tar_file
from statistics import mean

def MATTR(corpus, n = 500, tokenizer = None):
    """
    Calculates the Moving Average Type Token Ratio for each document in a given corpus

    Parameters
    ----------
    corpus : str
        The tarball containing the corpus
    n: int
        The window length over which to calculate
    tokenizer: function
        Optional: function to take in a line (str) and output a list of tokens (str[])

    Example
    ---------
    import corpustools.measure as ctm; ctm.MATTR('d:/working/corpus.tar')
    """

    corpus = pathlib.Path(corpus)

    measures_file = corpus.parent.joinpath('./MATTR.csv')
    if measures_file.exists():
        measures_file.unlink()
    if tokenizer == None:
        tokenizer = lambda line: [token.upper() for token in line.strip().split() if len(token) > 0]

    measures = _measure_corpus(corpus, n, tokenizer)
    _write_measures(measures_file, measures)

def _measure_corpus(corpus, n, tokenizer):

    print('Measuring MATTR...')
    measures = {}

    for (tar_info, tar_file) in file_in_corpus(corpus):
        lines = read_lines_from_tar_file(tar_file)
        flat_list = [token for line in lines for token in tokenizer(line)]
        measures[tar_info.name] = _measure_document(flat_list, n)

    return measures

def _measure_document(tokens, n):
    l = len(tokens)
    if l == 0:
        mattr = 0
        pass
    elif l <= n:
        mattr = len(set(tokens)) / l
        pass
    else:
        ttr = [0] * (l - n + 1)
        ttr_pos = 0
        dict = {}
        for i in range(0, n):
            token = tokens[i]
            if token not in dict:
                dict[token] = 0
                pass
            dict[token] = dict[token] + 1
        ttr[ttr_pos] = len(dict)
        ttr_pos = ttr_pos + 1
        for i in range(n, l):
            prior_token = tokens[i - n]
            dict[prior_token] = dict[prior_token] - 1
            token = tokens[i]
            if token not in dict:
                dict[token] = 0
            dict[token] = dict[token] + 1
            ttr[ttr_pos] = len(dict)
            ttr_pos = ttr_pos + 1
        mattr = mean(ttr)/n
    return round(mattr, 8)

def _write_measures(file_name, measures):

    print('Writing Measures...')
    write_dictionary(file_name, measures)
