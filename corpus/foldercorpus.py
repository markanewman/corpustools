from argparse import ArgumentParser
from ..measures.ttr import ttr

if __name__ == '__main__':
    parser = ArgumentParser()
    parser.add_argument('-m', '--measure', help = 'The measure to use', required = False, choices = ['basic', 'counts', 'ttr', 'mattr', 'coverage'])
    parser.add_argument('-in', '--folder-in', help = 'The folder to iterate over to use', required = False)
    parser.add_argument('-out', '--measurements', help = 'The file containing the measurements requested', required = False)
    args = parser.parse_args()
    print(f'measure: {args.measure}')
    print(f'measure: {args.folder_in}')
    print(f'measure: {args.measurements}')

    args.measure = 'ttr'
    args.folder_in ='d:/sample'
    args.measurements ='d:/sample.ttr.csv'

    measures = {'ttr': ttr.ttr }

    measures[args.measure](args.folder_in)

    
    
    print(f'TTR: {measure}')