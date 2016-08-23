#!/usr/bin/env/python

# same_first_last.py
# Code written by Robin Goyal
# Created on 19-08-2016
# Last updated on 19-08-2016

def same_first_last(nums):
    if (len(nums) >= 1 and nums[0] == nums[-1]):
        return True
    else:
        return False
