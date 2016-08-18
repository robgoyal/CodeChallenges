#!/usr/bin/env/python

# CutTheSticks.py
# Code written by Robin Goyal
# Created on 18-08-2016
# Last updated on 18-08-2016

n = int(raw_input().strip())
arr = map(int, raw_input().strip().split(' '))

while (len(arr) > 0):
    print len(arr)
    cut = min(arr)
    arr[:] = [x for x in arr if x != cut]
    arr[:] = [x - cut for x in arr]
