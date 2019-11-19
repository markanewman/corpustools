Tools for calculating linguistic measures

# Measures

There are 3 ways to calculate every measure:

* One file at a time
* One folder at a time
* One tar file at a time

Folders and tar files are effectivaly the same thing.
Tar files are much more convient when transfering corpuses via sneaker-net.
So offer the ability to calculate on them directly.

Below can be found a list of measures.
The listed syntax is for a single file.
When calculating over a folder (or tar file) use `python [folder|tar]corpus.py -m(easure) [{{measure name}}] -in {{folder path|tar path}} -out {{measures path}}`

Tokenization is always performed the same way:

* Words are seperated by a single space
* Puncunation is left as-is where-is.
  i.e. "See Bob run ." tokenizes to `['See', 'Bob', 'run', '.']` vs. "See Bob run." tokenizes to `['See', 'Bob', 'run.']`
* One sentence per line
* Pargraphes have a single enter seperating them


| Name | Status | Command |
|--- |--- |--- 
| Basic | | `python basic.py -f(ile) c:\foo.txt`
| Counts | | `python counts.py -f(ile) c:\foo.txt`
| TTR |  | `python ttr.py -f(ile) c:\foo.txt`
| MATTR |  | `python mattr.py -f(ile) c:\foo.txt`
| Coverage | | `python coverage.py -f(ile) c:\foo.txt -dict c:\zipfs.csv` 

**Basic**: Basic document lengths: words/document, sentences/document, paragraphs/document, mean words/sentence, mean words/paragraph, and mean sentences/paragraph

**Counts**: List of all the unique words and their total word counts.
Unlike other measures, this measure produces a list of results, not just one.

**TTR**: [Type-Token Ratio](https://en.wikipedia.org/wiki/Lexical_density)

**MATTR**: [Moving Average Type-Token Ratio](https://doi.org/10.1080/09296171003643098)

**Coverage**: What percentage of the document is accounted for by the given dictionary.
Most useful when testing [Zipf's Law](https://en.wikipedia.org/wiki/Zipf%27s_law)

# Transform

In addtion to the measures above, several bulk transformation tools are available as below.
Folder (and tar file) processing are available too using the `-t(ransform) {{transform name}}` argument.

| Name | Status | Command |
|--- |--- |--- 
| ToLower | | 
| Stem | | 
| FilterIn | | 
| FilterOut | | 

**ToLower**: Lowercases the entire file.

**Stem**: Stems all words in the file.

**FilterIn**: Filters the file, _KEEPING_ all words in the given dictionary.
Be careful of puncunation.
Be careful of case.

**FilterOut**: Filters the file, _DISCARDING_ all words in the given dictionary.
Be careful of puncunation.
Be careful of case.
