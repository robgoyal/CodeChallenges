#!/usr/bin/env/python

# date_fashion.py
# Code written by Robin Goyal
# Created on 18-08-2016
# Last updated on 18-08-2016

def date_fashion(you, date):
    if (you <= 2 or date <= 2):
        return 0
    elif (you >= 8 or date >= 8):
        return 2
    else:
        return 1
