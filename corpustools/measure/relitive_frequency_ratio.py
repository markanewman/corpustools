import pathlib
import progressbar as pb
from ..utils.csvfile import write_dictionary
from ..utils.tarfile import file_in_corpus, read_lines_from_tar_file
from statistics import mean

def relitive_frequency_ratio(domain_corpus, subdomain_corpus, tokenizer = None):
    """
    Measures the relitive frequency ratio of tokens in the subdomain compaired to the main domain.
    Tokens more strongly related to the domain are excluded from the final list

    Parameters
    ----------
    domain_corpus : str
        The tarball containing the domain's corpus
    subdomain_corpus : int
        The tarball containing the sub-domain's corpus
    tokenizer: function
        Optional: function to take in a line (str) and output a list of tokens (str[])

    Example
    ---------
    import corpustools.measure as ctm; ctm.relitive_frequency_ratio('d:/working/domain.tar', 'd:/working/subdomain.tar')
    """

    domain_corpus = pathlib.Path(domain_corpus)
    subdomain_corpus = pathlib.Path(subdomain_corpus)

    measures_file = subdomain_corpus.parent.joinpath('./rfr.csv')
    if measures_file.exists():
        measures_file.unlink()
    if tokenizer == None:
        tokenizer = lambda line: [token.upper() for token in line.strip().split() if len(token) > 0]

    domain_counts = _collect_counts(domain_corpus, tokenizer)
    subdomain_counts = _collect_counts(subdomain_corpus, tokenizer)
    measures = _measure(domain_counts, subdomain_counts)
    _write_measures(measures_file, measures)

    return (measures_file, mean(measures.values()))

def _collect_counts(corpus, tokenizer):

    print('Collecting Token Counts ...')
    counts = {}
    
    for (tar_info, tar_file) in file_in_corpus(corpus):                    
        for line in read_lines_from_tar_file(tar_file):
            for token in tokenizer(line):
                if token not in counts:
                    pass
                    counts[token] =  0
                counts[token] = counts[token] + 1
            pass
        pass        

    return counts

def _measure(counts_d, counts_s):

    print('Measuring Relitive Frequency Ratios...')
    result = {}

    widgets = [ pb.Percentage(), ' ', pb.Bar(marker = '.', left = '[', right = ']'), ' ', pb.ETA() ]

    total_d = 0
    total_s = 0
    for kvp in counts_d.items(): total_d = total_d + kvp[1]
    for kvp in counts_s.items(): total_s = total_s + kvp[1]

    with pb.ProgressBar(widgets = widgets, max_value = len(counts_s)) as bar:
        for kvp in counts_s.items():
            vs = kvp[1]
            vd = counts_d[kvp[0]] if kvp[0] in counts_d else 1
            rfr = (vs/total_s)/(vd/total_d)
            if rfr > 1:
                pass
                result[kvp[0]] = round(rfr, 8)
            i = i + 1
            bar.update(i)
        pass

    return result

def _write_measures(file_name, measures):

    print('Writing Measures...')
    write_dictionary(file_name, measures, value_sort = True, asc_sort = False)
