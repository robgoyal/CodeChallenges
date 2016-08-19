#!/usr/bin/env/python

# caught_speeding.py
# Code written by Robin Goyal
# Created on 18-08-2016
# Last updated on 18-08-2016

def caught_speeding(speed, is_birthday):
    if (speed <= 60) or (is_birthday and speed <= 65):
        return 0
    elif (61 <= speed <= 80) or (is_birthday and (66 <= speed <= 85)):
        return 1
    elif (speed >= 81) or (is_birthday and speed >= 86):
        return 2
