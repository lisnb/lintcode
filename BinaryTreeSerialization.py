#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: lisnb
# @Date:   2015-05-17 11:51:41
# @Last Modified by:   lisnb
# @Last Modified time: 2015-05-17 12:37:27


"""
Definition of TreeNode:
"""
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None



import Queue
class Solution:

    '''
    @param root: An object of TreeNode, denote the root of the binary tree.
    This method will be invoked first, you should design your own algorithm 
    to serialize a binary tree which denote by a root node to a string which
    can be easily deserialized by your own "deserialize" method later.
    '''
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
                r.append(th.val)
                q.put(th.left)
                q.put(th.right)
            else:
                r.append('#')

        return ','.join(r)


    '''
    @param data: A string serialized by your serialize method.
    This method will be invoked second, the argument data is what exactly
    you serialized at method "serialize", that means the data is not given by
    system, it's given by your own serialize method. So the format of data is
    designed by yourself, and deserialize it here as you serialize it in 
    "serialize" method.
    '''
    def deserialize(self, data):
        # write your code here
        if not data:
            return None
        vals = data.split(',')
        head = TreeNode(vals[0])
        i = 1
        q = Queue.Queue()
        q.put(head)
        #q.put(head.right)
        while not q.empty() and i<len(vals):
            th = q.get()
            if vals[i]!='#':
                th.left = TreeNode(vals[i])
                q.put(th.left)
            i+=1
            if i<len(vals):
                if vals[i]!='#':
                    th.right = TreeNode(vals[i])
                    q.put(th.right)
                i+=1
        return head 


if __name__ == '__main__':
    s = Solution()
    ss = '1,2,3,#,#,4,#,#,5' 
    head = s.deserialize(ss)
    ss = s.serialize(head)
    print ss
    head = s.deserialize(ss)
    ss = s.serialize(head)
    print ss





