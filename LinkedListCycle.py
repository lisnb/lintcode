#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: lisnb
# @Date:   2015-05-10 22:32:12
# @Last Modified by:   lisnb
# @Last Modified time: 2015-05-11 00:11:23


"""
Definition of ListNode
class ListNode(object):

    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""
class Solution:
    """
    @param head: The first node of the linked list.
    @return: True if it has a cycle, or false
    """
    def hasCycle(self, head):
        # write your code here

        if not head or not head.next:
            return False 

        p1 = head
        p2 = head.next

        while True:
            if p1 == p2:
                return True
            if not p2 or not p2.next:
                return False 
            p1 = p1.next
            p2 = p2.next.next 
            



