#!/usr/bin/env/python

# DynamicArray.py
# Code written by Robin Goyal
# Created on 29-08-2016
# Last updated on 29-08-2016

lastAns = 0
inp = map(int, raw_input().split())
arr = [[] for x in range(inp[0])]

for i in range(inp[1]):
    temp = map(int, raw_input().split())

    if temp[0] == 1:
        seq = (temp[1] ^ lastAns) % len(arr)
        arr[seq].append(temp[2])

    else:
        seq = (temp[1] ^ lastAns) % len(arr)
        lastAns = arr[seq][temp[2] % len(arr[seq])]
        print lastAns
