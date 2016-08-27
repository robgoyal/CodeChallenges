#!/usr/bin/env/python

# centered_average.py
# Code written by Robin Goyal
# Created on 26-08-2016
# Last updated on 26-08-2016

def centered_average(nums):

    nums.remove(max(nums))
    nums.remove(min(nums))

    return sum(nums)/len(nums)
