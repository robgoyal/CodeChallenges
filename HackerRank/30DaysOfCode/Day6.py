#!/usr/bin/env/python

# Day6.py
# Code written by Robin Goyal
# Created on 28-07-2016
# Last updated on 28-07-2016

N = int(raw_input())
variables = []

for i in range(N):
    variables.append(raw_input())

for index in variables:
    even = ""
    odd = ""
    for character in range(len(index)):
        if character % 2 == 0:
            even += index[character]
        else:
            odd += index[character]
    print even, odd
