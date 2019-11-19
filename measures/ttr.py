import _helper as h
from argparse import ArgumentParser
from statistics import mean

def ttr(lines):
    """
    Calculates the Type-Token Ratio for a given document

    Parameters
    ----------
    lines : str
        the lines in the document
    """

    l = h.lines_to_tokens(lines)
    tokens = [y for x in l for y in x]

    l = len(tokens)
    if l == 0:
        ttr = 0
        pass
    else:
        ttr = len(set(tokens)) / l
        pass
    return round(ttr, 8)

if __name__ == '__main__':
    parser = ArgumentParser()
    parser.add_argument('-f', '--file', help = 'File to measure', required = True)
    args = parser.parse_args()
    print(f'file: {args.file}')

    lines = h.read_lines_from_file(args.file)
    measure = ttr(lines)
    print(f'TTR: {measure}')
