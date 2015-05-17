#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: lisnb
# @Date:   2015-05-17 12:47:35
# @Last Modified by:   lisnb
# @Last Modified time: 2015-05-17 13:09:04

import Queue

"""
Definition of TreeNode:
"""
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None



class Solution:
    """
    @param preorder : A list of integers that preorder traversal of a tree
    @param inorder : A list of integers that inorder traversal of a tree
    @return : Root of a tree
    """
    def buildTree(self, preorder, inorder):
        # write your code here
        if not preorder or not inorder:
            return None
        return self.build(preorder, 0, inorder, 0, len(inorder)-1)


    def build(self, preorder, pre, inorder, b, e):
        print pre, b, e
        if b==e:
            return TreeNode(inorder[b])
        if b>e:
            return None
        i = inorder.index(preorder[pre])
        root = TreeNode(inorder[i])
        root.left = self.build(preorder, pre+1, inorder, b, i-1)
        root.right = self.build(preorder, pre+1+i-b, inorder, i+1, e)
        return root 

    def serialize(self, root):
        # write your code here
        r = []
        q = Queue.Queue()
        if not root:
            return ''
        q.put(root)
        while not q.empty():
            th = q.get()
            if th:
                r.append(str(th.val))
                q.put(th.left)
                q.put(th.right)
            else:
                r.append('#')

        return ','.join(r)
if __name__ == '__main__':
    s = Solution()
    pre = [6,2,3,4,5]
    # pre = [1,2,3,4,5]
    ino = [2,4,5,3,6]
    # ino = [5,4,3,2,1]
    head = s.buildTree(pre, ino)
    print s.serialize(head)
