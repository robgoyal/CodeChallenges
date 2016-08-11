#!/usr/bin/env/python

# CompareTheTriplets.py
# Code written by Robin Goyal
# Created on 10-08-2016
# Last updated on 10-08-2016

A = map(int, raw_input().strip().split(' '))
B = map(int, raw_input().strip().split(' '))

pointA = 0
pointB = 0

for i in range(len(A)):
    if A[i] > B[i]:
        pointA += 1
    elif B[i] > A[i]:
        pointB += 1

print pointA, pointB
