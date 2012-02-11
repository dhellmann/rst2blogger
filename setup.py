#!/usr/bin/env python

PROJECT = 'rst2blogger'

VERSION = '1.0'

# Bootstrap installation of Distribute
import distribute_setup
distribute_setup.use_setuptools()

from setuptools import setup, find_packages

from distutils.util import convert_path
from fnmatch import fnmatchcase
import os
import sys

try:
    long_description = open('README.rst', 'rt').read()
except IOError:
    long_description = ''

setup(
    name = PROJECT,
    version = VERSION,
    
    description = 'Convert reStructuredText to HTML then post on Blogger.com blogs',
    long_description = long_description,
    license = 'BSD',
    
    author = 'Doug Hellmann',
    author_email = 'doug.hellmann@gmail.com',

    url = 'http://www.doughellmann.com/projects/%s/' % PROJECT,

    classifiers = [ 'Development Status :: 4 - Beta',
                    'License :: OSI Approved :: BSD License',
                    'Programming Language :: Python',
                    'Programming Language :: Python :: 2',
                    'Programming Language :: Python :: 2.7',
                    'Environment :: Console',
                    ],

    platforms = ['Any'],

    provides=['rst2blogger',
              ],
    install_requires=[
        'pyquery>=1.1.1',
        'distribute',
        'docutils>=0.8.1',
        'gdata>=2.0.16',
        ],

    packages = find_packages(),
    include_package_data = True,

    entry_points = {
        'console_scripts': [ 'rst2blogger = rst2blogger.cli:main' ],
        },

    zip_safe=False,
    )
