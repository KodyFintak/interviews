# -*- coding: utf-8 -*-
"""setup.py"""

from setuptools import setup

setup(
    name='space',
    version='0.1',
    install_requires=['pytest'],
    packages=['space'],
    package_data={'space': ['tests/*', 'tests/**/*']},
)
