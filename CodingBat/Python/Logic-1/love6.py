#!/usr/bin/env/python

# love6.py
# Code written by Robin Goyal
# Created on 18-08-2016
# Last updated on 18-08-2016

def love6(a, b):
    if (a == 6 or b == 6 or abs(a-b) == 6 or (a+b) == 6):
        return True
    else:
        return False
