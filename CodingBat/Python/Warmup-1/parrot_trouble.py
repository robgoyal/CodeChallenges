#!/usr/bin/env/python

# parrot_trouble.py
# Code written by Robin Goyal
# Created on 17-08-2016
# Last updated on 17-08-2016

def parrot_trouble(talking, hour):
    if (talking and (hour > 20 or hour < 7)):
        return True
    else:
        return False
