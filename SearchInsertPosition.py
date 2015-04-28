#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: lisnb
# @Date:   2015-04-28 00:02:00
# @Last Modified by:   lisnb
# @Last Modified time: 2015-04-28 00:21:50

class Solution:
    """
    @param A : a list of integers
    @param target : an integer to be inserted
    @return : an integer
    """
    def searchInsert(self, A, target):
        # write your code here
        if len(A) == 0:
            return 0
        return self.search(A, target, 0, len(A)-1)
    
    def search(self, A, target, b, e):
        if A[b]>target:
            return b
        if A[e]<target:
            return e+1
        mid = (b+e)/2
        if A[mid] == target:
            return mid 
        if A[mid] > target:
            return self.search(A,target,b,e-1)
        else:
            return self.search(A, target, mid+1, e)

if __name__ == '__main__':
    s = Solution()
    A = [1,3,5,6]
    print s.searchInsert(A,0)



