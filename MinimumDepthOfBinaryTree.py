#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: lisnb
# @Date:   2015-05-07 18:14:09
# @Last Modified by:   lisnb
# @Last Modified time: 2015-05-07 18:17:25



"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        this.val = val
        this.left, this.right = None, None
"""
class Solution:
    """
    @param root: The root of binary tree.
    @return: An integer
    """ 
    def minDepth(self, root):
        # write your code here
		if not root:
			return 0
		# return min(self.minDepth(root.left), self.minDepth(root.right))+1
		lmd = self.minDepth(root.left)
		rmd = self.minDepth(root.right)
		if lmd == 0 or rmd == 0:
			return max(lmd, rmd)+1
		else:
			return min(lmd, rmd)+1