#! /usr/bin/env python
# -*- coding: UTF-8 -*-

__author__ = 'james'

with open('file.txt') as f:
    contents = f.read()

# print(contents)

class CustomOpen(object):
    def __init__(self, filename):
        print('open ', filename)
        self.file = open(filename)

    def __enter__(self):
        return self.file

    def __exit__(self, ctx_type, ctx_value, ctx_traceback):
        print('close ')
        self.file.close()

with CustomOpen('file.txt') as f:
    contents2 = f.read()

print(contents2)