#!/usr/bin/env/python

# Day7.py
# Code written by Robin Goyal
# Created on 28-07-2016
# Last updated on 28-07-2016

n = int(raw_input().strip())
arr = map(int, raw_input().strip().split())

for index in range(len(arr)):
    print arr[-1-index]
