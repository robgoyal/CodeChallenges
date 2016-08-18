#!/usr/bin/env/python

# monkey_trouble.py
# Code written by Robin Goyal
# Created on 17-08-2016
# Last updated on 17-08-2016

def monkey_trouble(a_smile, b_smile):
    if ((a_smile and b_smile) or (not(a_smile) and not(b_smile))):
        return True
    else:
        return False
