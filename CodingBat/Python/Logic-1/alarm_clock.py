#!/usr/bin/env/python

# alarm_clock.py
# Code written by Robin Goyal
# Created on 18-08-2016
# Last updated on 18-08-2016

def alarm_clock(day, vacation):
    if (not(vacation) and (1 <= day <= 5)):
        return "7:00"
    elif (not(vacation) and (day == 0 or day == 6)) or (vacation and (1 <= day <= 5)):
        return "10:00"
    else:
        return "off"
