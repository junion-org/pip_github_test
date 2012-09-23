#!/usr/bin/env python
# coding: utf-8
from setuptools import setup, find_packages
from pip_github_test import __author__, __version__, __license__

setup(
        name             = 'pip_github_test',
        version          = __version__,
        description      = 'Sample for installing python library from github using pip',
        license          = __license__,
        author           = __author__,
        author_email     = 'junion@junion.org',
        url              = 'https://github.com/junion-org/pip_github_test.git',
        keywords         = 'sample pip github python',
        packages         = find_packages(),
        install_requires = [],
        )

