#!/usr/bin/env/python

# near_ten.py
# Code written by Robin Goyal
# Created on 18-08-2016
# Last updated on 18-08-2016

def near_ten(num):
    if abs((num % 10) <= 2) or abs((num % 10) >= 8):
        return True
    else:
        return False
