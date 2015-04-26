#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: LiSnB
# @Date:   2015-04-26 17:30:36
# @Last Modified by:   LiSnB
# @Last Modified time: 2015-04-26 18:49:46



class Solution:
    # @param A, a list of integers
    # @return an integer
    def firstMissingPositive(self, A):
        # write your code here
        if not A:
            return 1
        i=0
        A.append(-1)
        while i<len(A):
            print A
            if A[i]<0 or A[i]>=len(A) or A[i]==i:
                i+=1
                continue
            if A[i] != A[A[i]]:
                t = A[A[i]]
                A[A[i]] = A[i]
                A[i]=t 
            else:
                i+=1
        # print A
        for i in range(1,len(A)):
            if A[i]!=i:
                return i
        return A[-1]+1

if __name__ == '__main__':
    s = Solution()
    A = [1,2,3]
    print s.firstMissingPositive(A)

