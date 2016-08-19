#!/usr/bin/env/python

# in1to10.py
# Code written by Robin Goyal
# Created on 18-08-2016
# Last updated on 18-08-2016

def in1to10(n, outside_mode):
    if (not(outside_mode) and (1 <= n <= 10)):
        return True
    elif (outside_mode and (n <= 1 or n >= 10)):
        return True
    else:
        return False
