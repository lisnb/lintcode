#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: LiSnB
# @Date:   2015-04-29 09:26:47
# @Last Modified by:   LiSnB
# @Last Modified time: 2015-04-29 10:37:06


class Solution:
    #@param A: An integers list.
    #@return: return any of peek positions.
    def findPeak(self, A):
        # write your code here
        if not A or len(A)<3:
            return None
        left, right = 0, len(A)-1
        while left<right:
            mid = left+(right-left)/2
            if A[mid]>A[mid-1] and A[mid]>A[mid+1]:
                return mid
            if A[mid]>A[mid+1]:
                right = mid 
            else:# A[mid]>A[mid-1]:
                left = mid 
            #else:
        return left


if __name__ == '__main__':
    A = [1, 2, 1, 3, 4, 8, 7, 6]
    s = Solution()
    print s.findPeak(A)