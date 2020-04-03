#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr  2 10:05:40 2020
@author: Govinda KC

Implementation of Queue using Singly Linked List
Time Complexity: O(1) (for adding and removing the items)

"""

import random

class Node:
    def __init__(self, data, next=None):
        self.data  = data
        self.next = next

class Queue:
    def __init__(self, head=None, tail = None):
        self.head = head
        self.tail = tail
    
    def Empty(self, L):
        if L.head==None:
            return True
        
    def Print(self, L):
        if self.Empty(L):
            print('Linked list is Empty')
            return
        temp = L.head
        count=1
        while temp:
            print(f"{count}--> {temp.data}")
            temp = temp.next
            count+=1
    def add(self, L, item):
        newnode = Node(item)
        if L.tail == None:
            L.head = L.tail = newnode
        else:
            L.tail.next = newnode
            L.tail = L.tail.next

    def remove(self, L):
        if L.head == None:
            return
        else:
            if L.head.next == None:
                # Last item 
                L.head = None
            else:
                temp = L.head.next
                L.head = temp
                L.head.next = temp.next
                   
        
if __name__ == '__main__':
    q = Queue() 
    A = [2,3,5,6,7]
    # A = [random.randint(0,100) for i in range(10)]
    
    L = Queue()
    for a in A:
        q.add(L, a)
        
    # Print Linked List  
    print("Linked List implementation of Queue")
    q.Print(L)
    
    for i in range(2):
        q.remove(L)
    # Print Linked List
    print('Linked List after removing items [First in First Out (FIFO)]')    
    q.Print(L)
