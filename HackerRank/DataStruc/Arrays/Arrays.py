#!/usr/bin/env/python

# Arrays.py
# Code written by Robin Goyal
# Created on 28-08-2016
# Last updated on 28-08-2016

array_length = int(raw_input())
inp = map(int, raw_input().split())

reverse_inp = inp[::-1]
for i in reverse_inp:
    print i,
