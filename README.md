# corpustools

Tools for manipulating a tar file based corpses

# Install

```{shell}
pip install git+https://github.com/markanewman/corpustools.git
```

# Tools

```{py}
import corpustools.rewrite as ctrw
import corpustools.measure as ctm;
```

## Single corpus tools

- [ ] Measure TTR
- [ ] Measure MATTR
- [ ] Count words per sentence/paragraph/document
- [ ] Count sentences per paragraph/document
- [x] Unique Words
```{py}
ctm.frequency_counts('d:/working/corpus.tar')
```
- [x] Zif's Law Coverage
```{py}
ctm.coverage('d:/working/corpus.tar', 'd:/working/tokens.csv')
```
- [ ] Filter out words
- [ ] Filter in words
- [ ] Split corpus into sub corpuses based on known split
- [x] Extract corpus into blocks of ~1M lines
```{py}
ctrw.tar_to_block_text('d:/working/corpus.tar', 1000000)"
```
- [ ] Create subcorpus based on exact text string

## Multi corpus tools

- [x] Compute relitive frequency ratio
```{py}
ctm.relitive_frequency_ratio('d:/working/domain.tar', 'd:/working/subdomain.tar')
```
