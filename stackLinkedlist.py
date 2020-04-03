#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr  2 10:05:40 2020
@author: Govinda KC

Implementation of Stack using Singly Linked List
Time Complexity: O(1) (for adding and removing the items)
"""

import random

class Node:
    def __init__(self, data, next=None):
        self.data  = data
        self.next = next

class Stack:
    def __init__(self, head=None, tail = None):
        self.head = head
        self.tail = tail
        self.count = 0
         
    def Print(self, L):
        temp = L.head
        while temp: 
            print(f"{temp.data}")
            # print(f"{self.count}--> {temp.data}")
            self.count -= 1
            temp = temp.next
            
    def push(self, L, item):
        
        newnode = Node(item)
        if L.tail == None:
            L.head = L.tail = newnode
            self.count += 1
        else:
            temp = L.head
            L.head = newnode
            L.head.next = temp
            self.count += 1

    def pop(self, L):
        if L.head == None:
            return
        else:
            temp = L.head.next
            L.head = temp
            L.head.next = temp.next
                             
        
if __name__ == '__main__':
    
    s = Stack()
    A = [2,3,5,6,7]
    # A = [random.randint(0,100) for i in range(10)]
    L = Stack()

    for a in A:
        s.push(L, a)
    
    print('List implementating Stack')    
    s.Print(L)
    
    for i in range(2):
        s.pop(L)
    print('List after removing items [Last in First Out (LIFO)]')
    s.Print(L)

    
        
        
        
