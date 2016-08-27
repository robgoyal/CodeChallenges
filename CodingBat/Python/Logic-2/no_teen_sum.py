#!/usr/bin/env/python

# no_teen_sum.py
# Code written by Robin Goyal
# Created on 27-08-2016
# Last updated on 27-08-2016

def no_teen_sum(a, b, c):

    a = fix_teen(a)
    b = fix_teen(b)
    c = fix_teen(c)

    return a + b + c

def fix_teen(n):

    if (13 <= n <= 14) or (16 < n <= 19):
        return 0
    else:
        return n
