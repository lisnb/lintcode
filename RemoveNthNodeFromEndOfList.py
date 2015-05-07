#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: LiSnB
# @Date:   2015-05-07 17:05:51
# @Last Modified by:   lisnb
# @Last Modified time: 2015-05-07 18:11:57


class Solution:
    """
    @param head: The first node of linked list.
    @param n: An integer.
    @return: The head of linked list.
    """
    def removeNthFromEnd(self, head, n):
        # write your code here
        thead = ListNode()
        thead.next = head
        p1 = head
        while n>0:
        	n-=1
        	p1=p1.next
        if not p1:
        	return head.next
        while p1.next:
        	p1=p1.next
        	thead = thead.next
        thead.next = thead.next.next
        return head 



        