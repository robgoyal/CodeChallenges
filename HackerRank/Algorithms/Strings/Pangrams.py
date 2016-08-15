#!/usr/bin/env/python

# Pangrams.py
# Code written by Robin Goyal
# Created on 14-08-2016
# Last updated on 14-08-2016

inp = raw_input()
chars = []


# Loops through string, checks if alphabet and lowercases the char
# if index exists in list then continue, otherwise append

for i in inp:
    if (i.isalpha()):
        i = i.lower()
        if i in chars:
            continue
        else:
            chars.append(i)

# Checks if chars contains all 26 alphabet characters
if len(chars) == 26:
    print "pangram"
else:
    print "not pangram"

