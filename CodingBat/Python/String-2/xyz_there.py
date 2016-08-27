#!/usr/bin/env/python

# xyz_there.py
# Code written by Robin Goyal
# Created on 27-08-2016
# Last updated on 27-08-2016

def xyz_there(str):

    xyz = False

    for i in range(len(str) - 2):
        if str[i:i+3] == "xyz":
            xyz = True
            if str[i-1] == ".":
                xyz = False

    return xyz
