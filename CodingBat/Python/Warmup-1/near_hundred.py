#!/usr/bin/env/python

# near_hundred.py
# Code written by Robin Goyal
# Created on 17-08-2016
# Last updated on 17-08-2016

def near_hundred(n):
    near_100 = 100 - n
    near_200 = 200 - n

    if (abs(near_100) <= 10 or abs(near_200) <= 10):
        return True
    else:
        return False
