#!/usr/bin/env/python

# close_far.py
# Code written by Robin Goyal
# Created on 27-08-2016
# Last updated on 27-08-2016

def close_far(a, b, c):
    if abs(a-b) <= 1 and (abs(a-c) >= 2 and abs(b-c) >= 2):
        return True
    elif abs(a-c) <= 1 and (abs(a-b) >= 2 and abs(b-c) >= 2):
        return True
    else:
        return False
