#!/usr/bin/env/python

# PlusMinus.py
# Code written by Robin Goyal
# Created on 10-08-2016
# Last updated on 10-08-2016

n = int(raw_input().strip())
arr = map(int, raw_input().strip().split(' '))

posNums = 0
negNums = 0
zeroNums = 0

for i in arr:
    if (i > 0):
        posNums += 1
    elif (i < 0):
        negNums += 1
    else:
        zeroNums += 1

print str(posNums/float(n)) + "\n" + str(negNums/float(n)) + "\n" + str(zeroNums/float(n))
