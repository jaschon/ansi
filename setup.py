#!/usr/bin/env python3

import os
from setuptools import setup
import ansi

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name = "ansi",
    version = ansi.__version__,
    author = ansi.__author__,
    description = (ansi.__doc__),
    keywords = "ANSI, Terminal, Escape Codes, Color",
    url = "https://github.com/jaschon/ansi",
    packages=['ansi', 'tests'],
    long_description=read('README.md'),
    test_suite="tests", 
)
