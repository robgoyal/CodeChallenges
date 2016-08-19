#!/usr/bin/env/python

# cigar_party.py
# Code written by Robin Goyal
# Created on 18-08-2016
# Last updated on 18-08-2016

def cigar_party(cigars, is_weekend):
    if (40 <= cigars <= 60):
        return True
    elif (is_weekend and cigars > 40):
        return True
    else:
        return False
