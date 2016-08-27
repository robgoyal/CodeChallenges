#!/usr/bin/env/python

# has22.py
# Code written by Robin Goyal
# Created on 26-08-2016
# Last updated on 26-08-2016

def has22(nums):

    for i in range(len(nums) - 1):
        if nums[i:i+2] == [2, 2]:
            return True

    return False
