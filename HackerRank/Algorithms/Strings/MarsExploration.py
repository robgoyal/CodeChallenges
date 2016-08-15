#!/usr/bin/env/python

# MarsExploration.py
# Code written by Robin Goyal
# Created on 15-08-2016
# Last updated on 15-08-2016

inp = raw_input().strip()
altered = 0

for index in range(len(inp)):
    if (index % 3 == 0 and inp[index] == "S"):
        continue
    elif (index % 3 == 1 and inp[index] == "O"):
        continue
    elif (index % 3 == 2 and inp[index] == "S"):
        continue
    else:
        altered += 1

print altered
