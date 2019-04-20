import tarfile
from io import BytesIO

def list_tar_files(tar_ball):
    """
    `getmembers()` requires scaning the entire file before returning the first value.
    Avoid that by making a looping iterator.
    """

    tar_info = tar_ball.next()
    while tar_info is not None:
        tar_file = tar_ball.extractfile(tar_info)
        if tar_file is not None:
            pass
            yield tar_info, tar_file
        tar_info = tar_ball.next()
    pass

def read_lines_from_tar_file(tar_file):
    """
    Read the tar file returning the lines
    """

    txt = tar_file.read()
    txt = txt.decode('utf-8')
    return txt.splitlines()

def write_lines_to_tarball(tarball, name, lines):
    """
    Writes the relevant wmd data to the tar ball
    """

    txt = '\n'.join(lines)
    txt = txt.encode('utf-8')
    with BytesIO(txt) as tar_file:
        info = tarfile.TarInfo(name = name)
        info.size = len(txt)
        tarball.addfile(info, fileobj = tar_file)
    pass