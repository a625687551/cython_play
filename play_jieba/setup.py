# -*- coding:utf-8 -*-

from distutils.core import setup
from Cython.Build import cythonize

# setup(name="hello world app", ext_modules=cythonize("viterbi_new.pyx"))
setup(name="hello world app", ext_modules=cythonize("./viterbi_new.pyx"))
