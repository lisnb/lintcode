#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: LiSnB
# @Date:   2015-04-26 15:05:02
# @Last Modified by:   LiSnB
# @Last Modified time: 2015-04-26 15:32:34



class Solution:
    """
    @param A: Given an integers array A
    @return: An integer array B and B[i]= A[0] * ... * A[i-1] * A[i+1] * ... * A[n-1]
    """
    def productExcludeItself(self, A):
        # write your code here
        if not A:
            return []
        if len(A)==1:
            return A
        lms, rms = [1], A[:]
        lm, rm = 1, 1
        for i in range(1,len(A)):
            lms.append(lms[i-1]*A[i-1])
        rms[-1]=1
        for i in range(len(A)-2, -1, -1):
            rms[i] = rms[i+1]*A[i+1]
        print lms, rms
        ms = []
        for i in range(len(A)):
            ms.append(lms[i]*rms[i])
        return ms

if __name__ == '__main__':
    # A = [1,2,3,4,5,6,7,0]
    A = [0]

    s = Solution()

    print s.productExcludeItself(A)