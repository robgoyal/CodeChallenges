#!/usr/bin/env/python

# Intro to Conditional Statements
# Code Written by Robin Goyal
# Created on July 11, 2016
# Last updated on July 11, 2016

inp = int(raw_input("Enter a number to test to see if it is Weird or Not Weird: "))

# Conditional test to see if the input is odd
# or if the input is even and in the range of 6 to 20

if (inp % 2 != 0) or (inp % 2 == 0 and inp in range(6, 21)):
    print "Weird"


# Conditional test to see if the input is odd and if its
# in the range of 2 to 5 or greater than 21

elif (inp % 2 == 0) and (inp in range(2, 6) or inp > 20):
    print "Not Weird"
