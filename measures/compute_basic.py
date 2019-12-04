from argparse import ArgumentParser
import csv
import pathlib
import progressbar as pb
import statistics as stats
import string

def collect_paragraphs(lines):
    """
    Splits lines into groups where the split is defined by a blank line
    """
    curr = 0
    start = -1
    for line in lines:
        has_tokens = len(line) > 0
        started = start != -1
        if has_tokens and (not started):
            start = curr
        elif (not has_tokens) and started:
            yield lines[start:curr]
            start = -1
        curr = curr + 1  
    if start != -1:
        yield lines[start:]        

def counts(paragraphs):

    ppd = len(paragraphs)
    spd = sum([len(paragraph) for paragraph in paragraphs])
    wpd = sum([sum([len(lines) for lines in paragraph]) for paragraph in paragraphs])

    return ppd, spd, wpd

def process_all_files(folder_in, measure_out):
    folder_in = pathlib.Path(folder_in)
    measure_out = pathlib.Path(measure_out)

    i = 1
    widgets = [ 'Processing File # ', pb.Counter(), ' ', pb.Timer(), ' ', pb.BouncingBar(marker = '.', left = '[', right = ']')]
    with pb.ProgressBar(widgets = widgets) as bar:
        with measure_out.open('w', encoding = 'utf-8', newline='') as measure_out:
            writer = csv.writer(measure_out, delimiter = ',', quotechar = '"', quoting = csv.QUOTE_ALL)
            writer.writerow(['filename', 'paragraphs_per_document', 'sentences_per_document', 'words_per_document'])
            for file_name in folder_in.iterdir():
                 if file_name.is_file():
                    bar.update(i)
                    i = i + 1

                    file_in = file_name
                    with file_in.open('r', encoding = 'utf-8') as file_in:
                        lines = [line.strip().split() for line in file_in.readlines()]
                        lines = [[token for token in line if token not in string.punctuation] for line in lines]
                        paragraphs = [paragraph for paragraph in collect_paragraphs(lines)]

                    ppd, spd, wpd = counts(paragraphs)        
                    writer.writerow([file_name.name, ppd, spd, wpd])

if __name__ == '__main__':
    parser = ArgumentParser()
    parser.add_argument('-in', '--folder-in', help = 'Folder to import files from', required = True)
    parser.add_argument('-out', '--measure-out', help = 'File used to save the measures', required = True)
    args = parser.parse_args()
    print(f'folder in: {args.folder_in}')
    print(f'measure out: {args.measure_out}')
    process_all_files(args.folder_in, args.measure_out)