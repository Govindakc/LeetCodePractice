#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr  2 12:41:09 2020

@author: Govinda KC

Leetcode problems: (1) 876. Middle of the Linked List
                   (2) 237. Delete Node in a Linked List
                   (3) 206. Reverse Linked List
                   (4) 234. Palindrom Linked List
HackerRank problems: insertNodeAtPosition 
"""

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # List
    # Constructor    
    def __init__(self, head = None, tail = None):
        self.head = head
        self.tail = tail
    
    def insertItems(self, val):
        if L.head == None:
            L.head = ListNode(val)
            L.tail = L.head
        else:
            L.tail.next = ListNode(val)
            L.tail = L.tail.next
    def getSize(self, head):
        count = 0
        while head:
            count += 1
            head = head.next
        return count

    def printList(self, L):
        while L:
            print(L.val)
            L = L.next 
        
    def reverseList(self, head):
        prev = None
        current = head
        
        while current:
            temp = current.next
            current.next = prev
            prev = current
            current = temp
            
        return prev
    
    def middleNode(self, head):
        slow = head
        fast = head
        
        while fast:
            if fast.next==None:
                return slow
            fast = fast.next.next
            slow = slow.next
            
        if fast == None:
            return slow
        else:
            return slow.next
        
    def deleteNode(self, L):
        L.val = L.next.val
        L.next = L.next.next

    def isPalindrome(self, head):
        new = []
        while head:
            new.append(head.val)
            head = head.next
        new2 = new[::-1]
        if new2 == new:
            return True
        return False
    
    def insertNodeAtPosition(self, head, val, position):
        counter = 0 
        node = ListNode(val)
        temp = node

        if self.getSize(head) < position:
            print('Index is out of range')
            return
 
        elif  position == 0:
            node.next = head
            return temp
        else:
            current = head
            while counter < (position-1):
                current = current.next
                counter+=1
            temp = current.next
            current.next = node
            node.next = temp
            return head
        
def main():
    # Create a Linked List
    for a in N:
        Solution().insertItems(a)
    
    print('Print Linked List')
    Solution().printList(L.head)
    
    # Get the middle node of the Linked List
    # If there are two middle nodes, return the second middle node
    
    mid = Solution().middleNode(L.head)

    print('Linked list from the middle')
    Solution().printList(mid)# not L.head or mid.head: (not the head of the list)
    
    # Insert a node at specific position
    temp = Solution().insertNodeAtPosition(L.head, 8, 4)
    print('Print Linked List after insertion')
    Solution().printList(temp) # not L.head or temp.head: (not the head of the list)
    # Delete the a node from a Linked List
    Solution().deleteNode(L.head.next)
    
    print('Linked List after deletion')
    Solution().printList(L.head)
    
    print('Check if the Linked List is Palindrome')
    print(Solution().isPalindrome(L.head))

    # Reverse Linked List
    reversedList = Solution().reverseList(L.head)

    print('Reversed Linked List')
    Solution().printList(reversedList)
    
if __name__ == '__main__':
    N = [3,2,2,1,6]
    L = Solution()
    main()
