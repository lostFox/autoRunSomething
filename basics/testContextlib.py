#! /usr/bin/env python
# -*- coding: UTF-8 -*-

__author__ = 'james'

from contextlib import contextmanager

@contextmanager
def custom_open(filename):
    f = open(filename)
    try:
        yield f
    finally:
        f.close()

with custom_open('file.txt') as f:
    contents = f.read()

print(contents)