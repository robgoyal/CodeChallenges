#!/usr/bin/env/python

# sum13.py
# Code written by Robin Goyal
# Created on 27-08-2016
# Last updated on 27-08-2016

def sum13(nums):

    count = 0

    for i in range(len(nums)):
        if nums[i] == 13:
            print "#1: %d" % i
            continue
        elif nums[i-1] == 13:
            print "#2: %d" % i
            continue
        else:
            print "#3: %d" % i
            count += nums[i]
    return count

print sum13([1, 2, 13, 2, 1, 13])
