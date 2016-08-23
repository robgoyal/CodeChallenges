#!/usr/bin/env/python

# common_end.py
# Code written by Robin Goyal
# Created on 19-08-2016
# Last updated on 19-08-2016

def common_end(a, b):
    if (a[0] == b[0]) or (a[-1] == b[-1]):
        return True
    else:
        return False
