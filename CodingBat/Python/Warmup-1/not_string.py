#!/usr/bin/env/python

# not_string.py
# Code written by Robin Goyal
# Created on 17-08-2016
# Last updated on 17-08-2016

def not_string(str):
    inp = str.split(' ')
    if (inp[0] == "not"):
        return str
    else:
        return "not " + str
