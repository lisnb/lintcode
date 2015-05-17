#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: lisnb
# @Date:   2015-05-10 20:58:45
# @Last Modified by:   lisnb
# @Last Modified time: 2015-05-10 22:25:39


# Definition for singly-linked list with a random pointer.
# class RandomListNode:
#     def __init__(self, x):
#         self.label = x
#         self.next = None
#         self.random = None
class Solution:
    # @param head: A RandomListNode
    # @return: A RandomListNode
    def copyRandomListWA(self, head):
        # write your code here
        if not head:
            return None
        nhead = RandomListNode(head.label)
        p1 = head.next
        p2 = nhead
        listmap = {}
        listmap[id(head)] = nhead
        while p1:
            p2.next = RandomListNode(p2.label)
            listmap[id(p1)] = p2
            p2 = p2.next
            p1 = p1.next 

        p1, p2 = head, nhead
        while p1:
            p2.random = listmap[id(p1.random)] if p1.random else None
            p1 = p1.next
            p2 = p2.next

        return nhead 

    def copyRandomList(self, head):
        if not head:
            return head

        p1 = head
        while p1:
            t = p1.next
            p1.next = RandomListNode(p1.label)
            p1.next.next = t 
            p1 = t 
        p1 = head 
        while p1:
            if p1.random:
                p1.next.random = p1.random.next
            p1 = p1.next.next

        nhead = head.next 
        p1 = nhead
        p2 = p1.next
        # 1 1 2 2 3 3 4 4
        while p2:
            # t = p2.next.next
            p1.next = p2.next
            p2.next = p2.next.next 
            p1 = p1.next
            p2 = p1.next
        return nhead 




