#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: lisnb
# @Date:   2015-05-10 21:18:56
# @Last Modified by:   lisnb
# @Last Modified time: 2015-05-10 21:35:58


"""
Definition of ListNode
class ListNode(object):

    def __init__(self, val, next=None):
        self.val = val
        self.next = next
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        this.val = val
        this.left, this.right = None, None
"""
class Solution:
    """
    @param head: The first node of linked list.
    @return: a tree node
    """
    def sortedListToBST(self, head):
        # write your code here
        array = []
        p1 = head
        while p1:
            array.append(p1.val)
            p1 = p1.next

        if not array:
            return None

        return self.sortedlisttobst(array, 0, len(array)-1)

    def sortedlisttobst(self, array, b ,e):
        if b>e:
            return None
        if b==e:
            return TreeNode(array[b])
        mid = b+(e-b)/2

        root = TreeNode(array[mid])
        root.left = self.sortedlisttobst(array, b, mid-1)
        root.right  = self.sortedlisttobst(array, mid+1, e)
        return root
