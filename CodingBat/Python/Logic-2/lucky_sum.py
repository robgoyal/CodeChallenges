#!/usr/bin/env/python

# lucky_sum.py
# Code written by Robin Goyal
# Created on 27-08-2016
# Last updated on 27-08-2016

def lucky_sum(a, b, c):

    if a == 13:
        return 0
    elif b == 13:
        return a
    elif c == 13:
        return a + b
    else:
        return a + b + c
