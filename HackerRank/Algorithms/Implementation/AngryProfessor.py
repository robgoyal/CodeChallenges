#!/usr/bin/env/python

# AngryProfessor.py
# Code written by Robin Goyal
# Created on 18-08-2016
# Last updated on 18-08-2016

numTests = int(raw_input().strip())

for a0 in xrange(numTests):
    n, k = raw_input().strip().split(' ')
    n, k = [int(n), int(k)]
    arr = map(int, raw_input().strip().split(' '))

    onTime = 0
    for i in arr:
        if i <= 0:
            onTime += 1

    if onTime < k:
        print "YES"
    else:
        print "NO"
