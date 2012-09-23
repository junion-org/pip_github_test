#!/usr/bin/env python
# coding: utf-8
from setuptools import setup, find_packages
from pip_github_test import *

setup(
        name             = __name__,
        version          = __version__,
        description      = __description__,
        license          = __license__,
        author           = __author__,
        author_email     = __author_email__,
        url              = __url__,
        keywords         = __keywords__,
        packages         = find_packages(),
        install_requires = __install_requires__,
        )

