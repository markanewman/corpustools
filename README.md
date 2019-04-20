# corpustools

Tools for manipulating a tar file based corpses

# Install

```{shell}
pip install git+https://github.com/markanewman/corpustools.git
```

# Tools

## Single corpus tools

- [ ] Measure TTR
- [ ] Measure MATTR
- [ ] Count words per sentence/paragraph/document
- [ ] Count sentences per paragraph/document
- [ ] Filter out words
- [ ] Filter in words
- [ ] Split corpus into sub corpuses based on known split
- [x] Extract corpus into blocks of ~1M lines
```{shell}
python -c "import corpustools.rewrite as ctrw; ctrw.tar_to_block_text('d:/working/corpus.tar', 1000000)"
```
- [ ] Create subcorpus based on exact text string

## Multi corpus tools

- [x] Compute relitive frequency ratio
```{shell}
python -c "import corpustools.measure as ctm; ctm.relitive_frequency_ratio('d:/working/domain.tar', 'd:/working/subdomain.tar')"
```
