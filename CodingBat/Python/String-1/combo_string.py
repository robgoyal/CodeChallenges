#!/usr/bin/env/python

# combo_string.py
# Code written by Robin Goyal
# Created on 18-08-2016
# Last updated on 18-08-2016

def combo_string(a, b):
    if len(b) < len(a):
        return "%s%s%s" % (b, a, b)
    else:
        return "%s%s%s" % (a, b, a)
