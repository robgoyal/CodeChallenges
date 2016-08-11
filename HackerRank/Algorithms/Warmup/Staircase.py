#!/usr/bin/env/python

# Staircase.py
# Code written by Robin Goyal
# Created on 10-08-2016
# Last updated on 10-08-2016

N = int(raw_input())

for i in range(N):
    print (N-1-i) * " " + (i+1) * "#"
