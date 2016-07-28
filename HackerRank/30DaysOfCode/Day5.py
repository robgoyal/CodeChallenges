#!/usr/bin/env/python

# Day5.py
# Code written by Robin Goyal
# Created on 28-07-2016
# Last updated on 28-07-2016

import sys

N = int(raw_input().strip())

for multiple in range(1, 11):
    print "%d x %d = %d" % (N, multiple, N * multiple)
