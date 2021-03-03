#!/usr/bin/env python
# -*- coding: utf-8 -*-

import bisect

def new_tax(salary, exempt=5000):
    if salary < exempt:
        return 0.0

    above = salary - exempt

    ranges = [0,3000, 12000,25800,35000, 55000, 88000]
    rate = [.03, .1,.2,.25,30,.35,.45]

    i = bisect.bisect_left(ranges, above)
    j = 0
    tax = 0.0
    while j< i:
        if j+1< i:

            tax += (ranges[j+1]- ranges[j]) * rate[j]
        else:

            tax += (above-ranges[j])*rate[j]

        j += 1

    return tax

print(new_tax(10000, 5000))