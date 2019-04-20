import pathlib
from ..utils.tarfile import file_in_corpus, read_lines_from_tar_file

def tar_to_block_text(corpus, line_count):
    """
    Rewrites a single tar based corpus into several files.
    Some programs do not like to process over tar files.
    In this case break the tar file into several txt files with approxmitly x lines per file.
    Will not break a single file in the corpus accross multipul text files.

    Parameters
    ----------
    corpus : str
        The tarball containing text only files
    line_count : int
        The _approximate_ number of lines per file

    Example
    ---------
    import corpustools.rewrite as ctrw; ctrw.tar_to_block_text('d:/working/corpus.tar', 1000000)
    """
    corpus = pathlib.Path(corpus)
    root = corpus.parent.joinpath('./block_text')
    if root.exists():
        _delete_folder(root)
    root.mkdir(exist_ok = True)

    file_count = 0
    lines_buffer = {}
    lines_buffer_count = 0

    for (tar_info, tar_file) in file_in_corpus(corpus):
        lines = read_lines_from_tar_file(tar_file)
        lines = [line.strip() for line in lines]
        lines = [line + '\n' for line in lines if len(line) > 0]

        lines_buffer[tar_info.name] = lines
        lines_buffer_count = lines_buffer_count + len(lines)

        if lines_buffer_count >= line_count:
            file_count = file_count + 1
            file = root.joinpath('./part-{0:06d}.txt'.format(file_count))
            with open(file, 'w', encoding = 'utf-8', newline = '') as file:
                for key in lines_buffer:
                    file.writelines(['------ {0} ------\n'.format(key)])
                    file.writelines(lines_buffer[key])
                    pass
                pass
            lines_buffer = {}
            lines_buffer_count = 0
    pass


def _delete_folder(pth) :
    for sub in pth.iterdir() :
        if sub.is_dir() :
            delete_folder(sub)
        else :
            sub.unlink()
    pth.rmdir()