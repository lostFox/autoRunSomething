# test_runtime.py
from __future__ import print_function

from integ import integrate_f
import time

f = lambda x: x**2-x

def py_inte(a, b, N):
    s = 0
    dx = (b-a) / N
    for i in range(N):
        s += f(a + i * dx)
    return s * dx

if __name__ == '__main__':
    start = time.clock()
    for k in xrange(1000):
        py_inte(-10, 10, 1000)
    print('pure python takes {}'.format(time.clock() - start))

    start = time.clock()
    for k in xrange(1000):
        integrate_f(-10, 10, 1000)
    print('cython take {}'.format(time.clock() - start))