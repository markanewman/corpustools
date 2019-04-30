# modified from https://github.com/pypa/sampleproject/blob/master/setup.py

from setuptools import setup, find_packages
from os import path

here = path.abspath(path.dirname(__file__))
with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name = 'corpustools',
    version = '0.0.5',
    description = 'Tools for manipulating a tar file based corpses',
    long_description = long_description,
    long_description_content_type = 'text/markdown',
    url = 'https://github.com/markanewman/corpustools',
    author = '@markanewman',
    classifiers = [
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Linguists',
        'Topic :: Language Processing :: Corpus Tools',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3'
    ],
    keywords = 'language-processing data-science corpus-linguistics',
    packages = find_packages(exclude=['contrib', 'docs', 'tests']),
    python_requires='>=3.5, <4',
    install_requires = ['progressbar2'],
    project_urls = {
        'Bug Reports': 'https://github.com/markanewman/corpustools/issues',
        'Source': 'https://github.com/markanewman/corpustools/',
    }
)