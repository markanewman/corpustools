from argparse import ArgumentParser
import csv
import math
import pathlib
import progressbar as pb
import statistics as stats
import string

def compute_mattr(tokens, n):
    """
    Calculates the Moving Average Type Token Ratio

    Parameters
    ----------
    tokens : array
        The list of tokens to measure
    n: int
        The window length over which to calculate
    """

    l = len(tokens)
    if l == 0:
        mattr = 0
    elif l <= n:
        mattr = len(set(tokens)) / l
    else:
        ttr = [0] * (l - n + 1)
        ttr_pos = 0
        dict = {}
        for i in range(0, n):
            token = tokens[i]
            if token not in dict:
                dict[token] = 0
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
        mattr = stats.mean(ttr)/n
    return mattr

def process_all_files(folder_in, measure_out, window_length):
    folder_in = pathlib.Path(folder_in)
    measure_out = pathlib.Path(measure_out)

    i = 1
    widgets = [ 'Processing File # ', pb.Counter(), ' ', pb.Timer(), ' ', pb.BouncingBar(marker = '.', left = '[', right = ']')]
    with pb.ProgressBar(widgets = widgets) as bar:
        with measure_out.open('w', encoding = 'utf-8', newline='') as measure_out:
            writer = csv.writer(measure_out, delimiter = ',', quotechar = '"', quoting = csv.QUOTE_ALL)
            writer.writerow(['filename', f'mattr{window_length}'])
            for file_name in folder_in.iterdir():
                 if file_name.is_file():
                    bar.update(i)
                    i = i + 1

                    file_in = file_name
                    with file_in.open('r', encoding = 'utf-8') as file_in:
                        lines = [line.strip().split() for line in file_in.readlines()]
                        lines = [[token for token in line if token not in string.punctuation] for line in lines]
                        lines = [line for line in lines if len(line) > 0]                        
                    
                    tokens = [x for y in lines for x in y]
                    result = round(compute_mattr(tokens, window_length), 8)
                    writer.writerow([file_name.name, result])

if __name__ == '__main__':
    parser = ArgumentParser()
    parser.add_argument('-in', '--folder-in', help = 'Folder to import files from', required = True)
    parser.add_argument('-out', '--measure-out', help = 'File used to save the measures', required = True)
    parser.add_argument('-len', '--window_length', help = 'The window length to use for the moving average', required = True, type = int)
    args = parser.parse_args()
    print(f'folder in: {args.folder_in}')
    print(f'measure out: {args.measure_out}')
    print(f'window length: {args.window_length}')
    process_all_files(args.folder_in, args.measure_out, args.window_length)