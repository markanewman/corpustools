from argparse import ArgumentParser
import csv
import math
import pathlib
import progressbar as pb
import statistics as stats
import string

def compute_ttr(tokens):
    """
    Calculates the Type Token Ratio

    Parameters
    ----------
    tokens : array
        The list of tokens to measure
    """

    l = len(tokens)
    if l == 0:
        ttr = 0
    else:
        ttr = len(set(tokens)) / l
    return ttr

def process_all_files(folder_in, measure_out):
    folder_in = pathlib.Path(folder_in)
    measure_out = pathlib.Path(measure_out)

    i = 0
    widgets = [ 'Processing File # ', pb.Counter(), ' ', pb.Timer(), ' ', pb.BouncingBar(marker = '.', left = '[', right = ']')]
    with pb.ProgressBar(widgets = widgets) as bar:
        with measure_out.open('w', encoding = 'utf-8', newline='') as measure_out:
            writer = csv.writer(measure_out, delimiter = ',', quotechar = '"', quoting = csv.QUOTE_ALL)
            writer.writerow(['filename', 'ttr'])
            for file_name in folder_in.iterdir():
                 if file_name.is_file():
                    bar.update(i)
                    i = i + 1

                    file_in = file_name
                    with file_in.open('r', encoding = 'utf-8') as file_in:
                        lines = [line.strip().split() for line in file_in.readlines()]
                        lines = [line for line in lines if len(line) > 0]
                        lines = [[token for token in line if token not in string.punctuation] for line in lines]

                    tokens = [x for y in lines for x in y]
                    result = round(compute_ttr(tokens), 8)                
                    writer.writerow([file_name.name, result])

if __name__ == '__main__':
    parser = ArgumentParser()
    parser.add_argument('-in', '--folder-in', help = 'Folder to import files from', required = True)
    parser.add_argument('-out', '--measure-out', help = 'File used to save the measures', required = True)
    args = parser.parse_args()
    print(f'folder in: {args.folder_in}')
    print(f'measure out: {args.measure_out}')
    process_all_files(args.folder_in, args.measure_out)