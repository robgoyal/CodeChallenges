#!/usr/bin/env/python

# DivisibleSumPairs.py
# Code written by Robin Goyal
# Created on 15-08-2016
# Last updated on 15-08-2016

n, k = raw_input().strip().split(' ')
n, k = [int(n), int(k)]
a = map(int, raw_input().strip().split(' '))

pairs = 0
for i in range(n):
    for j in range(i+1, n):
        if ((a[i] + a[j]) % k == 0):
            pairs += 1

print pairs
