#!/usr/bin/env/python

# Day12.py
# Code written by Robin Goyal
# Created on 31-07-2016
# Last updated on 31-07-2016

class Person:

    def __init__(self, firstName, lastName, idNumber):
        self.firstName = firstName
        self.lastName = lastName
        self.idNumber = idNumber

    def printPerson(self):
        print "Name: ", self.lastName + ",", self.firstName
        print "ID: ", self.idNumber


class Student(Person):

    def __init__(self, firstName, lastName, idNumber, scores):
        Person.__init__(self, firstName, lastName, idNumber)
        self.scores = scores

    def calculate(self):
        scoreSum = 0
        for index in self.scores:
            scoreSum += index

        averageScore = scoreSum/len(self.scores)

        if 90 <= averageScore <= 100:
            return "O"
        elif 80 <= averageScore < 90:
            return "E"
        elif 70 <= averageScore < 80:
            return "A"
        elif 55 <= averageScore < 70:
            return "P"
        elif 40 <= averageScore < 55:
            return "D"
        else:
            return "T"

line = raw_input().split()
firstName = line[0]
lastName = line[1]
idNum = line[2]
numScores = int(raw_input())
scores = map(int, raw_input().split())
s = Student(firstName, lastName, idNum, scores)
s.printPerson()
print "Grade: ", s.calculate()
