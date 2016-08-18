#!/usr/bin/env/python

# diff21.py
# Code written by Robin Goyal
# Created on 17-08-2016
# Last updated on 17-08-2016

def diff21(n):
    diff = n - 21
    if (n > 21):
        return 2 * abs(diff)
    else:
        return abs(diff)
