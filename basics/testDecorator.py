#! /usr/bin/env python
# -*- coding: UTF-8 -*-

__author__ = 'james'

def foo():
    print('foo')

def decorator(func):
    return func

foo = decorator(foo)    #手动装饰

@decorator
def bar():
    print("bar")

foo()
