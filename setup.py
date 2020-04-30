#!/usr/bin/env python

import sys, os, shutil
from distutils.core import setup

setup(name='preloadify',
      version='1.0',
      description='Create fat binaries with ease.',
      author='Tobias Glaesser',
      url='https://github.com/tobimensch/preloadify/',
      scripts=['preloadify'],
      packages=['preloadify'],
      install_requires=['docopt']
     )
