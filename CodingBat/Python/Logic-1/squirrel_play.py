#!/usr/bin/env/python

# squirrel_play.py
# Code written by Robin Goyal
# Created on 18-08-2016
# Last updated on 18-08-2016

def squirrel_play(temp, is_summer):
    if (60 <= temp <= 90):
        return True
    elif (is_summer and 60 <= temp <= 100):
        return True
    else:
        return False
