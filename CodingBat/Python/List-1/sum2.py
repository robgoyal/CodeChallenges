#!/usr/bin/env/python

# sum2.py
# Code written by Robin Goyal
# Created on 19-08-2016
# Last updated on 19-08-2016

def sum2(nums):
    if len(nums) >= 2:
        return nums[0] + nums[1]
    elif len(nums) == 1:
        return nums[0]
    else:
        return 0
