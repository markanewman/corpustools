from argparse import ArgumentParser

if __name__ == '__main__':
    parser = ArgumentParser()
    parser.add_argument('-f', '--file', help = 'File to measure', required = False)
    args = parser.parse_args()
    print(f'file: {args.file}')

    lines = h.read_lines_from_file(args.file)
    measure = ttr(lines)
    print(f'TTR: {measure}')