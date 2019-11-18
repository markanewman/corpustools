import pathlib
import tarfile
from ..utils.csvfile import read_dictionary
from ..utils.tarfile import file_in_corpus, read_lines_from_tar_file, write_lines_to_tarball

def filter_in_tokens(corpus, tokens, tokenizer = None):
    """
    Rewrites a single tar based corpus keeping only the given list of tokens

    Parameters
    ----------
    corpus : str
        The tarball containing the corpus
    tokens: str
        The file containing the list of tokens to keep
    tokenizer: function
        Optional: function to take in a line (str) and output a list of tokens (str[])

    Example
    ---------
    import corpustools.rewrite as ctrw; ctrw.filter_in_tokens('d:/working/corpus.tar', 'd:/working/tokens.csv')
    """

    corpus = pathlib.Path(corpus)
    tokens = pathlib.Path(tokens)

    rewrite_tarball = corpus.parent.joinpath('./rewrite.tar')
    if rewrite_tarball.exists():
        rewrite_tarball.unlink()
    if tokenizer == None:
        tokenizer = lambda line: [token.upper() for token in line.strip().split() if len(token) > 0]

    tokens = set(read_dictionary(tokens).keys())
    _rewrite(corpus, tokens, tokenizer, rewrite_tarball)

    return rewrite_tarball

def _rewrite(corpus, tokens, tokenizer, tar_ball_out):

    print('Re-Writing Corpus...')

    with tarfile.open(tar_ball_out, 'w') as tar_ball_out:
        for (tar_info, tar_file) in file_in_corpus(corpus):
            lines = read_lines_from_tar_file(tar_file)
            lines = [[token for token in tokenizer(line) if token in tokens] for line in lines]
            lines = [' '.join(line) for line in lines]
            write_lines_to_tarball(tar_ball_out, tar_info.name, lines)
        pass
    pass
