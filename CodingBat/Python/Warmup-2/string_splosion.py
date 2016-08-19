#!/usr/bin/env/python

# string_splosion.py
# Code written by Robin Goyal
# Created on 18-08-2016
# Last updated on 18-08-2016

def string_splosion(str):
    inp = ""
    for i in range(len(str)):
        inp += str[0:i]
    return inp + str
