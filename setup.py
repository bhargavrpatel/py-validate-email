# -*- coding: utf-8 -*-
from setuptools import setup, find_packages


def read(x):
    return open(os.path.join(os.path.dirname(__file__), x)).read()


tests_require = ['pytest', 'coverage', 'tox']
description = 'A Python port to validate disposable emails'
readme = read('README.rst')
changelog = read('ChangeLog.rst')

setup(
    name='py-validate-email',
    version='1.0.2',
    description=description,
    long_description=readme + '\n' + changelog,
    keywords='validate disposable emails',
    author='Bhargav Patel',
    author_email='ziikutv@gmail.com',
    url='https://github.com/bhargavrpatel/py-validate-email',
    license='MIT',
    classifiers=[
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy',
        'Operating System :: OS Independent',
    ],
    packages=find_packages(exclude=['tests']),
    install_requires=[],
    extras_require={
        'tests': tests_require,
    },
    entry_points={
        'console_scripts': [
        ],
    },
)
