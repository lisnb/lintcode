#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: LiSnB
# @Date:   2015-05-07 14:06:52
# @Last Modified by:   LiSnB
# @Last Modified time: 2015-05-07 15:24:11


"""
Definition of SegmentTreeNode:
"""
class SegmentTreeNode:
    def __init__(self, start, end, max):
        self.start, self.end, self.max = start, end, max
        self.left, self.right = None, None


class Solution: 
    # @param start, end: Denote an segment / interval
    # @return: The root of Segment Tree
    def build(self, start, end):
        # write your code here
        if start>end:
            return None
        root = SegmentTreeNode(start, end)
        if start == end:
            return root 
        mid = start + (end-start)/2
        root.left = self.build(start, mid)
        root.right = self.build(mid+1, end)
        return root

    def show(self, root):
        if not root:
            return 
        print '[', root.start, ', ', root.end, ']'
        self.show(root.left)
        self.show(root.right)

    def query(self, root, start, end):
        if not root:
            return 0
        if root.start == root.end:
            return root.max 
        if root.start == start and root.end == end:
            return root.max
        mid = root.start + (root.end-root.start)/2;
        if mid >=end:
            return self.query(root.left, start, end)
        if mid<=start:
            return self.query(root.right, start, end)
        else:
            return max(self.query(root.left, start, mid), self.query(root.right, mid+1, end))



if __name__ == '__main__':
    s = Solution()
    root = s.build(0,6)
    s.show(root)
