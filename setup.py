#!/usr/bin/env python3.9

from setuptools import setup



setup(
    name='dupoff',
    version='0.0.1',
    author='Javier Montalvo',
    author_email='buitrejma@gmail.com',
    py_modules=['dupoff.df'],
    packages=['dupoff'],
    python_requires='>=3.9',
    description='Takes off duplicate sequences from fasta file and writes unique sequences to new fasta file',
    long_description = open('README.md', 'r').read(),
    install_requires =['click', 'biopython'],
    license = 'GNU General Public License v3 or later (GPLv3+)',
    url='https://www.github.com/exseivier/not-alike',
    entry_points = {
        'console_scripts' : [
                'dupoff=dupoff.df:main'
                ]
            },
    classifiers = [
        'Development Status :: 3 - Alpha',
        'Environment :: Console',
        'Intended Audience :: End Users/Desktop',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python :: 3.9',
        'Topic :: Scientific/Engineering :: Bio-Informatics',
        ],
        )
