#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: LiSnB
# @Date:   2015-05-07 14:06:52
# @Last Modified by:   LiSnB
# @Last Modified time: 2015-05-07 14:14:47


"""
Definition of SegmentTreeNode:
"""
class SegmentTreeNode:
    def __init__(self, start, end):
        self.start, self.end = start, end
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




if __name__ == '__main__':
    s = Solution()
    root = s.build(1,1)
    s.show(root)
