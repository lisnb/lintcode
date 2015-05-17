#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: lisnb
# @Date:   2015-05-10 13:08:35
# @Last Modified by:   lisnb
# @Last Modified time: 2015-05-10 13:35:11
import time


"""
Definition of ListNode
"""
class ListNode(object):

    def __init__(self, val, next=None):
        self.val = val
        self.next = next

class Solution:
    """
    @param head: The first node of linked list.
    @param x: an integer
    @return: a ListNode 
    """

    # 4 -> 3 -> 2 -> 5 -> 2
    def partition(self, head, x):
        # write your code here
        if not head:
            return head 

        p1, p2 = ListNode(-1), ListNode(-1)
        p1.next, p2.next = head, head
        nhead = p1
        while p2.next and p2.next.val<x:
            p2 = p2.next
            

        while p2.next:
            print p2.val
            time.sleep(0.5)
            if p2.next.val>=x:
                p2=p2.next
            else:
                t = p1.next
                p1.next = p2.next
                p1 = p1.next
                p2.next = p1.next
                p1.next = t 
        return nhead.next

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
    l = [4,3,2,5,2]
    head = s.create(l)
    s.show(head)
    nhead = s.partition(head, 3)
    s.show(nhead)
