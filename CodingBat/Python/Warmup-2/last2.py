#!/usr/bin/env/python

# last2.py
# Code written by Robin Goyal
# Created on 18-08-2016
# Last updated on 18-08-2016

def last2(str):
    count = 0
    for i in range(len(str)-2):
        if str[len(str)-2:] == str[i:i+2]:
            count += 1
    return count
