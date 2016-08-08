#!/usr/bin/env/python

# Day17.py
# Code written by Robin Goyal
# Created on 07-08-2016
# Last updated on 07-08-2016

class Calculator:
    def __init__(self):
        self.name = 'Calculator'

    def power(self, n, p):
        self.n = n
        self.p = p

        if (n < 0) or (p < 0):
            raise ValueError("n and p should be non-negative")
        else:
            return pow(self.n, self.p)

myCalculator = Calculator()
T = int(raw_input())
for i in range(T):
    n, p = map(int, raw_input().split())
    try:
        ans = myCalculator.power(n, p)
        print ans
    except Exception, e:
        print e
