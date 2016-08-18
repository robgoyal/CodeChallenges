#!/usr/bin/env/python

# front_back.py
# Code written by Robin Goyal
# Created on 18-08-2016
# Last updated on 18-08-2016

def front_back(str):
    if len(str) <= 1:
        return str
    else:
        return str[-1] + str[1:len(str)-1] + str[0]
