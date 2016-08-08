#!/usr/bin/env/python

# Day20.py
# Code written by Robin Goyal
# Created on 08-08-2016
# Last updated on 08-08-2016

import sys

n = int(raw_input().strip())
a = map(int, raw_input().strip().split(' '))
numSwaps = 0

def swap(x, y):
    temp = a[x]
    a[x] = a[y]
    a[y] = temp

for i in range(n):
    for j in range(n-1):
        if a[j] > a[j+1]:
            swap(j, j+1)
            numSwaps += 1
    if numSwaps == 0:
        break

print "Array is sorted in %d swaps." % numSwaps
print "First Element: %d" % a[0]
print "Last Element: %d" % a[n-1]
