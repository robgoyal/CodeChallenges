#!/usr/bin/env/python

# SparseArrays.py
# Code written by Robin Goyal
# Created on 28-08-2016
# Last updated on 28-08-2016

N = int(raw_input())
strings = [raw_input() for i in range(N)]
numQueries = int(raw_input())

for i in range(numQueries):
    query = raw_input()
    print strings.count(query)
