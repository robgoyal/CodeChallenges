#!/usr/bin/env/python

# Day8.py
# Code written by Robin Goyal
# Created on 28-07-2016
# Last updated on 28-07-2016

n = int(raw_input())
phonebook = {}

for i in range(n):
    temp = raw_input().split(' ')
    phonebook[temp[0]] = temp[1]

lookup = raw_input()
while (len(lookup) > 0):
    if lookup in phonebook:
        print "%s=%s" % (lookup, phonebook[lookup])
    else:
        print "Not found"

    lookup = raw_input()

