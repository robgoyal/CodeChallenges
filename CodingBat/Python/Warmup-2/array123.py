#!/usr/bin/env/python

# array123.py
# Code written by Robin Goyal
# Created on 18-08-2016
# Last updated on 18-08-2016

def array123(nums):
    if ''.join(map(str, [1, 2, 3])) in ''.join(map(str, nums)):
        return True
    else:
        return False
