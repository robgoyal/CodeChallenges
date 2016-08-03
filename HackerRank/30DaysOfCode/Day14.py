#!/usr/bin/env/python

# Day14.py
# Code written by Robin Goyal
# Created on 02-08-2016
# Last updated on 02-08-2016

class Difference:
    def __init__(self, a):
        self.__elements = a

    def computeDifference(self):
        self.maximumDifference = 0

        for i in range(len(self.__elements)):
            for j in range(i+1, len(self.__elements)):
                tempMax = abs(self.__elements[i] - self.__elements[j])
                if tempMax > self.maximumDifference:
                    self.maximumDifference = tempMax

        return self.maximumDifference

_ = raw_input()
a = [int(e) for e in raw_input().split(' ')]

d = Difference(a)
d.computeDifference()

print d.maximumDifference
