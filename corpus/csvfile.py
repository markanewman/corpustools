import csv
import progressbar as pb

def write_dictionary(file_name, dictionary, value_sort = False, asc_sort = True):

    widgets = [ pb.Percentage(), ' ', pb.Bar(marker = '.', left = '[', right = ']'), ' ', pb.ETA() ]

    with pb.ProgressBar(widgets = widgets, max_value = len(dictionary)) as bar:
        with open(file_name, 'w', encoding = 'utf-8', newline = '') as file_name:
            writer = csv.writer(file_name, delimiter = ',', quotechar = '"', quoting = csv.QUOTE_ALL)
            writer.writerow(['key', 'value'])
            i = 0
            sort_index = 1 if value_sort else 0
            for kvp in sorted(dictionary.items(), key = lambda kv: kv[sort_index], reverse = not asc_sort):
                writer.writerow([kvp[0], kvp[1]])
                i = i + 1
                bar.update(i)
            pass
        pass
    pass

def read_dictionary(file_name):

    print('Reading tokens...')
    result = {}

    with open(file_name, 'r', encoding = 'utf-8', newline = '') as file_name:
        reader = csv.reader(file_name, delimiter = ',', quotechar = '"', quoting = csv.QUOTE_ALL)
        next(reader, None)
        for row in reader:
            result[row[0]] = row[1]
            pass
        pass

    return result