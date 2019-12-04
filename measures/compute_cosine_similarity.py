from argparse import ArgumentParser
import csv
import math
import pathlib
import progressbar as pb
import statistics as stats
import string

def compute_tf(lines):
    tf = {}

    for line in lines:
        for token in line:
            if token not in tf:
                tf[token] = 0
            tf[token] = tf[token] + 1

    return tf

def compute_idf(lines):
    idf = {}
    line_count = len(lines)

    for line in lines:
        for token in line:
            if token not in idf:
                lines_with_token_count = sum(1 for line in lines if token in line)
                idf[token] = 1 + math.log(line_count / (1 + lines_with_token_count))

    return idf

def compute_cosine_similarity(lines, idf):
    sim = [None] * len(lines)
    weight = lambda tf, idf, token: tf[token] * idf[token]

    doc_tf = compute_tf(lines)
    doc_vector = frozenset([x for y in lines for x in y])    
    denominator1 = math.sqrt(sum(weight(doc_tf, idf, token)**2 for token in doc_vector))

    for i in range(len(lines)):
        line = lines[i]
        line_tf = compute_tf([line])
        line_vector = frozenset(line)        
        common_tokens = doc_vector & line_vector
        numerator = sum(weight(doc_tf, idf, token) * weight(line_tf, idf, token) for token in common_tokens)
        denominator2 = math.sqrt(sum(weight(line_tf, idf, token)**2 for token in line_vector))
        sim[i] = numerator/(denominator1*denominator2)

    return sim

def process_all_files(folder_in, measure_out):
    folder_in = pathlib.Path(folder_in)
    measure_out = pathlib.Path(measure_out)

    i = 1
    widgets = [ 'Processing File # ', pb.Counter(), ' ', pb.Timer(), ' ', pb.BouncingBar(marker = '.', left = '[', right = ']')]
    with pb.ProgressBar(widgets = widgets) as bar:
        with measure_out.open('w', encoding = 'utf-8', newline='') as measure_out:
            writer = csv.writer(measure_out, delimiter = ',', quotechar = '"', quoting = csv.QUOTE_ALL)
            writer.writerow(['filename', 'mean', 'sd'])
            for file_name in folder_in.iterdir():
                 if file_name.is_file():
                    bar.update(i)
                    i = i + 1

                    file_in = file_name
                    with file_in.open('r', encoding = 'utf-8') as file_in:
                        lines = [line.strip().split() for line in file_in.readlines()]
                        lines = [[token for token in line if token not in string.punctuation] for line in lines]
                        lines = [line for line in lines if len(line) > 0]
                    
                    idf = compute_idf(lines)
                    result = compute_cosine_similarity(lines,  idf)
                    result_mean = stats.mean(result)
                    result_sd = stats.stdev(result) if len(result) > 1 else 0
                    writer.writerow([file_name.name, result_mean, result_sd])

if __name__ == '__main__':
    parser = ArgumentParser()
    parser.add_argument('-in', '--folder-in', help = 'Folder to import files from', required = True)
    parser.add_argument('-out', '--measure-out', help = 'File used to save the measures', required = True)
    args = parser.parse_args()
    print(f'folder in: {args.folder_in}')
    print(f'measure out: {args.measure_out}')
    process_all_files(args.folder_in, args.measure_out)