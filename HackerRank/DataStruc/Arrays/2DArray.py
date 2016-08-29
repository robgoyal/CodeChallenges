#!/usr/bin/env/python

# Day11.py
# Code written by Robin Goyal
# Created on 28-07-2016
# Last updated on 28-07-2016

arr = []
for arr_i in xrange(6):
    arr_temp = map(int, raw_input().strip().split(' '))
    arr.append(arr_temp)

hourglasses = []
for x in range(4):
    for y in range(4):
        hourglassSum = arr[x][y] + arr[x][y+1] + arr[x][y+2] + arr[x+1][y+1] + \
                arr[x+2][y] + arr[x+2][y+1] + arr[x+2][y+2]

        hourglasses.append(hourglassSum)
print max(hourglasses)
