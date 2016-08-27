#!/usr/bin/env/python

# count_evens.py
# Code written by Robin Goyal
# Created on 26-08-2016
# Last updated on 26-08-2016

def count_evens(nums):

    count_evens = 0

    for i in nums:
        if (i % 2) == 0:
            count_evens += 1

    return count_evens
