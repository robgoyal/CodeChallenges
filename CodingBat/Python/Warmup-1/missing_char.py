#!/usr/bin/env/python

# missing_char.py
# Code written by Robin Goyal
# Created on 17-08-2016
# Last updated on 17-08-2016

def missing_char(str, n):
    return str[:n] + str[n+1:]
