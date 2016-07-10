#!/usr/bin/env/python

# Day 2: Operators
# Code written by Robin Goyal
# Created on July 9, 2016
# Last Updated on July 9, 2016

# Calculating the total meal cost

# User inputs for meal, tip, and tax

mealCost = float(raw_input("What is the cost of the meal: "))
tipPercent = float(raw_input("How much you would like to tip as a percent: "))
taxPercent = float(raw_input("What is the tax percent: "))

# Cost calculation

totalCost = round(mealCost + mealCost * tipPercent / 100 + mealCost * taxPercent  / 100)

print "The total meal cost is %d dollars." % totalCost

