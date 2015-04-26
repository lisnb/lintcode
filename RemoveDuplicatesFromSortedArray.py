#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: LiSnB
# @Date:   2015-04-26 14:34:50
# @Last Modified by:   LiSnB
# @Last Modified time: 2015-04-26 14:41:19

class Solution:
    """
    @param A: a list of integers
    @return an integer
    """
    def removeDuplicates(self, A):
        # write your code here
        if not A:
            return 0
        p1, p2 = 0, 1
        while p2<len(A):
            if A[p2]!=A[p1]:
                p1+=1
                A[p1], A[p2] = A[p2], A[p1]
            p2+=1
        return p1+1

if __name__ == '__main__':
    s = Solution()
    A = [1,1,2,2,2,2,2,3,3,3,3,3,3,4,5,6]
    print s.removeDuplicates(A)
    print A
