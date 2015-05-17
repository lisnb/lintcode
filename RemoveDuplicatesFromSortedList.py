#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: lisnb
# @Date:   2015-05-10 01:44:26
# @Last Modified by:   lisnb
# @Last Modified time: 2015-05-10 01:49:07


"""
Definition of ListNode
class ListNode(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""
class Solution:
    """
    @param head: A ListNode
    @return: A ListNode
    """
    def deleteDuplicates(self, head):
        # write your code here
        if not head or not head.next:
            return head
        p1, p2 = head, head.next

        while p2:
            if p1.val == p2.val:
                p2 = p2.next
            else:
                p1.next = p2
                p1 = p1.next
        p1.next = None

        return head
