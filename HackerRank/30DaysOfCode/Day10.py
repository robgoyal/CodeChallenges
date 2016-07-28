#!/usr/bin/env/python

# Day10.py
# Code written by Robin Goyal
# Created on 28-07-2016
# Last updated on 28-07-2016

n = int(raw_input().strip())
binary_n = bin(n)[2:]
elements = []
count = 0
for i in binary_n:
    if int(i) == 1:
        count += 1
    elif int(i) == 0:
        elements.append(count)
        count = 0

print max(elements)
