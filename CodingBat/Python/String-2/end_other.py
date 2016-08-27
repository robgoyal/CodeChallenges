#!/usr/bin/env/python

# end_other.py
# Code written by Robin Goyal
# Created on 26-08-2016
# Last updated on 26-08-2016

def end_other(a, b):

    a = a.lower()
    b = b.lower()

    if len(a) > len(b):
        for i in range(len(a)):
            if a[len(a) - len(b):] == b:
                return True
            else:
                return False

    else:
        for i in range(len(b)):
            if b[len(b) - len(a):] == a:
                return True
            else:
                return False
