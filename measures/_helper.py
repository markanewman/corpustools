import pathlib

def read_lines_from_file(document):
    document = pathlib.Path(document)
    with open(document, 'r', encoding = 'utf-8') as document:
        return document.readlines()

def lines_to_tokens(lines):
    tokenizer = lambda line: [token for token in line.strip().split() if len(token) > 0]
    lines2 = [tokenizer(line) for line in lines]
    return lines2
