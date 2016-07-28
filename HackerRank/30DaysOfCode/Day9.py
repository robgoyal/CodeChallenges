#!/usr/bin/env/python

# Day9.py
# Code written by Robin Goyal
# Created on 28-07-2016
# Last updated on 28-07-2016

inp = int(raw_input())

def factorial(n):
    if n < 1:
        return 1
    else:
        return n * factorial(n-1)

print factorial(inp)
