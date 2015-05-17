#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: lisnb
# @Date:   2015-05-10 13:35:20
# @Last Modified by:   lisnb
# @Last Modified time: 2015-05-10 14:06:49



# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param head: the list
    # @param k: rotate to the right k places
    # @return: the list after rotation
    def rotateRight(self, head, k):
        # write your code here

        if not head:
            return None
        thead = head 
        l = 0
        while thead:
            l+=1
            thead = thead.next 
        k = k%l
        if k==0:
            return head 

        thead = head
        i = l-k-1 
        while i>0:
            thead = thead.next 
            i-=1
        nhead = thead.next
        thead.next = None
        thead = nhead
        
        while thead.next:
            thead = thead.next
        thead.next = head 
        return nhead

    def create(self, l):
        head = ListNode(l[0])
        thead = head
        i = 1
        while i<len(l):
            # t = ListNode(l[i])
            thead.next = ListNode(l[i])
            thead = thead.next
            i+=1

        return head 

    def show(self, head):
        thead = head 
        l = []
        while thead:
            l.append(str(thead.val))
            thead = thead.next 
        print ' -> '.join(l)


if __name__ == '__main__':
    s = Solution()
    l = [1,2,3,4,5,6,7]
    head = s.create(l)
    s.show(head)
    nhead = s.rotateRight(head, 7)
    s.show(nhead)

