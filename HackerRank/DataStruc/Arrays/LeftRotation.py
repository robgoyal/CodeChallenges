#!/usr/bin/env/python

# LeftRotation.py
# Code written by Robin Goyal
# Created on 28-08-2016
# Last updated on 28-08-2016

inp = map(int, raw_input().split())
arr = map(int, raw_input().split())

shift = inp[1] % inp[0]
newArr = arr[shift:] + arr[:shift]

for i in newArr:
    print i,
