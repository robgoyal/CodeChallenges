#!/usr/bin/env/python

# string_match.py
# Code written by Robin Goyal
# Created on 18-08-2016
# Last updated on 18-08-2016

def string_match(a, b):
    count = 0
    for i in range(len(a)-1):
        if a[i:2+i] == b[i:2+i]:
            count += 1
    return count
