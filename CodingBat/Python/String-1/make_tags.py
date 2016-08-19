#!/usr/bin/env/python

# make_tags.py
# Code written by Robin Goyal
# Created on 18-08-2016
# Last updated on 18-08-2016

def make_tags(tag, word):
    return "<%s>%s</%s>" % (tag, word, tag)
