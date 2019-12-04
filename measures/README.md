# Measures

Below is a list of lingustic measures.
Unless otherwise noted, each measure operates over an entire folder producing a single CSV file with one row per file.

Tokenization is always performed the same way:

* Pargraphes have a single enter seperating them
* One sentence per line
* Words are seperated by a single space
* Puncunation is left as-is where-is.
  i.e. "See Bob run ." tokenizes to `['See', 'Bob', 'run', '.']` vs. "See Bob run." tokenizes to `['See', 'Bob', 'run.']`

Unless otherwise noted, single punctuation tokens are filtered out.

* "See Bob run ." filters to `['See', 'Bob', 'run']`
* "See Bob run." filters to `['See', 'Bob', 'run.']`
* "See Bob run ..." filters to `['See', 'Bob', 'run', '...']`

| Name | Command |
|--- |--- 
| Basic | 
| Counts | 
| TTR |  `python compute_ttr.py -in d:/sample -out d:/ttr.csv`
| MATTR | `python compute_mattr.py -len 500 -in d:/sample -out d:/mattr.csv`
| Coverage | 
| Cosine Similarity | `python compute_cosine_similarity.py -in d:/sample -out d:/cosine.csv`

Remember to be in the `./measures` folder before running the commands.

**Basic**: Basic document lengths: words/document, sentences/document, paragraphs/document, mean words/sentence, mean words/paragraph, and mean sentences/paragraph

**Counts**: List of all the unique words and their total word counts.
Unlike other measures, this measure produces a list of results for the whole folder, not by-file.

**TTR**: Computes the [Type-Token Ratio](https://en.wikipedia.org/wiki/Lexical_density).
Filters out empty lines before calculation.

**MATTR**: Computes the [Moving Average Type-Token Ratio](https://doi.org/10.1080/09296171003643098).
Filters out empty lines before calculation.

**Coverage**: What percentage of the document is accounted for by the given dictionary.
Most useful when testing [Zipf's Law](https://en.wikipedia.org/wiki/Zipf%27s_law)

**Cosine Similarity**: Computes the cosine similarity between the document vector and the sentence vector.
Records both the mean and standard deviation.
Filters out empty lines before calculation.
The smoothed version of IDF is used in the calculation.