#!/usr/bin/env python3

import os
from setuptools import setup
from terminize import terminize

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name = "Terminizer",
    version = terminize.__version__,
    author = terminize.__author__,
    description = (terminize.__doc__),
    keywords = "Escape Codes, ANSI",
    url = "https://github.com/jaschon/terminize",
    packages=['terminize', 'tests'],
    long_description=read('README.md'),
)
