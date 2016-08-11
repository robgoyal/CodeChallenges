#!/usr/bin/env/python

# CircularArrayRotation.py
# Code written by Robin Goyal
# Created on 10-08-2016
# Last updated on 10-08-2016

commands = map(int, raw_input().split())
arr = map(int, raw_input().split())

for i in range(commands[1]):
    arr.insert(0, arr.pop())

for j in range(commands[2]):
    index = int(raw_input())
    print arr[index]
