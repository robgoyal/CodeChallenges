#!/usr/bin/env/python

# pos_neg.py
# Code written by Robin Goyal
# Created on 17-08-2016
# Last updated on 17-08-2016

def pos_neg(a, b, negative):
    if (not(negative) and (a < 0 or b < 0) and (a > 0 or b > 0)):
        return True
    elif (negative and (a < 0 and b < 0)):
        return True
    else:
        return False
