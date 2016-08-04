#!/usr/bin/env/python

# Day15.py
# Code written by Robin Goyal
# Created on 04-08-2016
# Last updated on 04-08-2016

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Solution:
    def display(self, head):
        current = head
        while current:
            print current.data,
            current = current.next

    def insert(self, head, data):
        new_node = Node(data)
        if (head == None):
            return new_node

        else:
            current = head
            while current:
                if (current.next == None):
                    current.next = new_node
                    break
                current = current.next
            return head

mylist = Solution()
T = int(input())
head = None
for i in range(T):
    data = int(input())
    head = mylist.insert(head, data)
mylist.display(head)
