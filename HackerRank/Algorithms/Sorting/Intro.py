#!/usr/bin/env/python

# Intro.py
# Code written by Robin Goyal
# Created on 14-08-2016
# Last updated on 14-08-2016

value = int(raw_input())
size = int(raw_input())
arr = map(int, raw_input().strip().split(' '))

for index in range(size):
    if arr[index] == value:
        print index
