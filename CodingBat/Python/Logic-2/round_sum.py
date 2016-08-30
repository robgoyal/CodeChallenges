#!/usr/bin/env/python

# round_sum.py
# Code written by Robin Goyal
# Created on 27-08-2016
# Last updated on 27-08-2016

def round_sum(a, b, c):

    a = round10(a)
    b = round10(b)
    c = round10(c)

    return a + b + c

def round10(num):

    if (num % 10 < 5):
        return num / 10 * 10
    else:
        return (num + 10) / 10 * 10
