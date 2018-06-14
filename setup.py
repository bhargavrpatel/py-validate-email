#!/usr/bin/env python
# -*- coding: utf-8 -*-

# This file is part of py-validate-email.
# https://github.com/bhargavrpatel/py-validate-email

# Licensed under the MIT license:
# http://www.opensource.org/licenses/MIT-license
# Copyright (c) 2018, Bhargav Patel <ziikutv@gmail.com>

from setuptools import setup, find_packages
from py_validate_email import __version__

tests_require = [
    'mock',
    'nose',
    'coverage',
    'yanc',
    'preggy',
    'tox',
    'ipdb',
    'coveralls',
    'sphinx',
]

description = 'A Python port to validate disposable emails'

setup(
    name='py-validate-email',
    version=__version__,
    description='A Python port to validate disposable emails',
    long_description=description,
    keywords='validate disposable emails',
    author='Bhargav Patel',
    author_email='ziikutv@gmail.com',
    url='https://github.com/bhargavrpatel/py-validate-email',
    license='MIT',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Operating System :: Unix',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: Implementation :: PyPy',
        'Operating System :: OS Independent',
    ],
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        # add your dependencies here
        # remember to use 'package-name>=x.y.z,<x.y+1.0' notation (this way you get bugfixes)
    ],
    extras_require={
        'tests': tests_require,
    },
    entry_points={
        'console_scripts': [
            # add cli scripts here in this form:
            # 'py-validate-email=py_validate_email.cli:main',
        ],
    },
)
