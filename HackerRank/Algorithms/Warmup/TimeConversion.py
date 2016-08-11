#!/usr/bin/env/python

# TimeConversion.py
# Code written by Robin Goyal
# Created on 10-08-2016
# Last updated on 10-08-2016

time = raw_input().strip().split(':')

if time[2][2:] == "AM":
    time[0] = str((int(time[0]) + 12) % 12)
    print str("{0:0>2}".format(time[0])) + ":%s:%s" % (time[1], time[2][0:2])
elif time[2][2:] == "PM":
    time[0] = str((int(time[0]) % 12) + 12)
    print "%s:%s:%s" % (time[0], time[1], time[2][0:2])


