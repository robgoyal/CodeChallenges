#!/usr/bin/env/python

# CamelCase.py
# Code written by Robin Goyal
# Created on 14-08-2016
# Last updated on 14-08-2016

inp = raw_input().strip()

# Initial word will be 1 since first letter is not uppercase
numWords = 1

for index in inp:
    if index.isupper():
        numWords += 1

print numWords
