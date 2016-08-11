#!/usr/bin/env/python

# AVeryBigSum.py
# Code written by Robin Goyal
# Created on 10-08-2016
# Last updated on 10-08-2016

# Same as ArraySum in Python

n = int(raw_input().strip())
arr = map(int, raw_input().strip().split(' '))

arraySum = 0;
for i in arr:
    arraySum += i

print arraySum
