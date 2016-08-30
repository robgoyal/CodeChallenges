#!/usr/bin/env/python

# sum67.py
# Code written by Robin Goyal
# Created on 27-08-2016
# Last updated on 27-08-2016

def sum67(nums):

#    if 6 in nums:
#        num6 = nums.count(6)
#        for i in range(num6):
#            del nums[nums.index(6):nums.index(7) + 1]

    while (6 in nums):
        del nums[nums.index(6):nums.index(7) + 1]
    return sum(nums)

print sum67([1, 2, 2])
print sum67([1, 2, 2, 6, 99, 99, 7])
print sum67([1, 1, 6, 7, 2])
print sum67([1, 6, 2, 2, 7, 1, 6, 99, 99, 7])
print sum67([1, 6, 2, 6, 2, 7, 1, 6, 99, 99, 7])
print sum67([2, 7, 6, 2, 6, 7, 2, 7])
print sum67([2, 7, 6, 2, 6, 2, 7])
print sum67([1, 6, 7, 7])
print sum67([6, 7, 1, 6, 7, 7])
print sum67([6, 8, 1, 6, 7])
print sum67([])
print sum67([6, 7, 11])
print sum67([11, 6, 7, 11])
print sum67([2, 2, 6, 7, 7])
