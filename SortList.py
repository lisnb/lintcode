#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: lisnb
# @Date:   2015-05-11 23:43:06
# @Last Modified by:   lisnb
# @Last Modified time: 2015-05-12 00:11:21



"""
Definition of ListNode
"""
class ListNode(object):

    def __init__(self, val, next=None):
        self.val = val
        self.next = next

class Solution:
    """
    @param head: The first node of the linked list.
    @return: You should return the head of the sorted linked list,
                  using constant space complexity.
    """
    def sortList(self, head):
        # write your code here
        self.sortlist(head, None)
        return head

    def sortlist(self, head, tail):
        if head == tail or head.next == tail:
            return 
        inorder = True
        p1 = head
        while p1.next != tail:
            if p1.val > p1.next.val:
                inorder = False
            p1 = p1.next
        if inorder:
            return 
        head.val, head.next.val = head.next.val, head.val
        pivot = head.val
        p1 = head 
        p2 = head.next 
        while p2!=tail:
            if p2.val < pivot:
                p1 = p1.next
                p1.val, p2.val = p2.val, p1.val
            p2 = p2.next 
        
        self.show(head)
        head.val, p1.val = p1.val, head.val
        self.sortlist(head, p1)
        self.sortlist(p1.next, tail)



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
    # l = [3,5,5,5,5,5,9,1,8,2,4]
    l = '1->3->3->1->3->1->3->3->2->3->2->2->1->1->1->3->2->2->1->1->2->2->2->3->3->1->1->2->2->2->1->2->1->1->2->3->3->2->2->3->2->3->2->2->2->1->1->3->2->3->3->1->1->1->2->2->1->2->2->2->2->3->1->3->1->1->1->2->1->2->2->2->1->3->2->2->2->3->3->2->3->3->1->1->2->2->1->2->1->3->2->1->3->3->1->2->1->1->1->1->1->2->1->2->2->2->2->3->3->3->1->1->3->2->1->1->2->1->3->3->2->2->1->3->1->3->1->3->2->2->3->2->3->2->2->1->2->3->1->3->1->2->3->3->2->3->3->3->1->1->2->3->1->2->3->2->1->1->2->3->1->1->3->1->2->2->3->2->1->3->1->2->1->3->2->1->1->2->2->2->1->3->1->3->2->3->3->1->1->3->1->2->1->2->3->1->2->1->1->3->1->3->3->1->1->1->2->2->1->3->1->2->2->3->2->1->3->2->1->3->2->2->3->3->2->2->1->3->2->2->2->2->2->3->2->2->3->1->3->2->1->3->2->1->2->3->3->3->1->2->2->3->1->1->2->2->3->2->1->1->1->1->1->3->2->2->2->1->3->2->1->2->3->2->1->1->2->1->3->3->1->3->1->2->2->1->2->3->2->3->3->1->2->3->2->2->3->3->2->1->3->2->2->2->3->3->3->1->1->2->1->1->2->3->3->3->1->3->2->2->1->2->2->1->2->3->1->3->2->2->3->3->3->1->2->3->2->1->3->1->1->2'.split('->')
    s = Solution()
    head = s.create(l)
    # s.show(head)
    nhead = s.sortList(head)
    s.show(nhead)
