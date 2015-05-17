#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: lisnb
# @Date:   2015-05-17 11:47:31
# @Last Modified by:   lisnb
# @Last Modified time: 2015-05-17 11:50:06




"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        this.val = val
        this.left, this.right = None, None
"""
class Solution:
    """
    @param root: The root of the binary search tree.
    @param k1 and k2: range k1 to k2.
    @return: Return all keys that k1<=key<=k2 in ascending order.
    """     
    def searchRange(self, root, k1, k2):
        # write your code here
        r = []
        self.searchrange(root, k1, k2)
        return r 

    def searchrange(self, root, k1, k2, r):
        if not root:
            return 
        self.searchrange(root.left, k1, k2, r)
        if k1<= root.val <=k2:
            r.append(root.val)
        self.searchrange(root.right, k1, k2,r )
