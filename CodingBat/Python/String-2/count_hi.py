#!/usr/bin/env/python

# count_hi.py
# Code written by Robin Goyal
# Created on 26-08-2016
# Last updated on 26-08-2016

def count_hi(str):

    count_hi = 0
    for i in range(len(str) - 1):
        if str[i:i+2] == "hi":
            count_hi += 1
    return count_hi
