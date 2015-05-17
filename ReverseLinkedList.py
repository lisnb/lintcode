#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: lisnb
# @Date:   2015-05-10 13:08:16
# @Last Modified by:   lisnb
# @Last Modified time: 2015-05-10 13:08:18



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
    @return: You should return the head of the reversed linked list. 
                  Reverse it in-place.
    """
    def reverse(self, head):
        # write your code here
        if not head:
            return None
        t, nhead = self.reverseit(head)
        return nhead
        
    def reverseit(self, head):
        if not head.next:
            return head, head
        t = head.next 
        head.next = None
        lhead, nhead = self.reverseit(t)
        lhead.next = head
        return head, nhead

