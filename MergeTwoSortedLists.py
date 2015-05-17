#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: lisnb
# @Date:   2015-05-10 01:38:35
# @Last Modified by:   lisnb
# @Last Modified time: 2015-05-10 01:45:32


"""
Definition of ListNode
class ListNode(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""
class Solution:
    """
    @param two ListNodes
    @return a ListNode
    """
    def mergeTwoLists(self, l1, l2):
        # write your code here
        if not l1:
        	return l2
        if not l2:
        	return l1

        head = None

        if l1.val<l2.val:
        	head = l1
        	l1 = l1.next
        else:
        	head = l2
        	l2 = l2.next 
        thead = head 
        while l1 and l2:
        	if l1.val<l2.val:
        		thead.next = l1
        		l1 = l1.next
        	else:
        		thead.next = l2
        		l2 = l2.next 
        	thead = thead.next

        if not l1:
        	thead.next = l2
        if not l2:
        	thead.next = l1
        return head

