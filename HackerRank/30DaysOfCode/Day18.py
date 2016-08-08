#!/usr/bin/env/python

# Day18.py
# Code written by Robin Goyal
# Created on 08-08-2016
# Last updated on 08-08-2016

class Solution:

    def __init__(self):
        self.stack = []
        self.queue = []

    def pushCharacter(self, char):
        self.stack = [char] + self.stack

    def enqueueCharacter(self, char):
        self.queue.append(char)

    def popCharacter(self):
        return self.stack.pop(0)

    def dequeueCharacter(self):
        return self.queue.pop(0)

# Modified this line to replace all whitespace to check for multi-word palindromes

strInp = raw_input().replace(" ", "")
print strInp
pDrome = Solution()

length = len(strInp)

for i in range(length):
    pDrome.pushCharacter(strInp[i])
    pDrome.enqueueCharacter(strInp[i])

isPalindrome = True

for i in range(length/2):
    if pDrome.popCharacter() != pDrome.dequeueCharacter():
        isPalindrome = False
        break

if isPalindrome:
    print "The word, " +strInp+ ", is a palindrome."
else:
    print "The word, " +strInp+ ", is not a palindrome."
