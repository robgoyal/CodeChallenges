#!/usr/bin/env/python

# array_count9.py
# Code written by Robin Goyal
# Created on 18-08-2016
# Last updated on 18-08-2016

def array_count9(nums):
    count = 0
    for i in nums:
        if i == 9:
            count += 1

    return count
