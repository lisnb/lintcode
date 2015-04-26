#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: lisnb
# @Date:   2015-04-26 22:54:09
# @Last Modified by:   lisnb
# @Last Modified time: 2015-04-26 23:41:19


class Solution:
    #@param A and B: sorted integer array A and B.
    #@return: A new sorted integer array
    def mergeSortedArray(self, A, B):
        # write your code here
        if not A and not B:
            return []
        if not A:
            return B 
        if not B:
            return A

        re = []
        p1, p2=0,0
        while p1<len(A) and p2<len(B):
            if A[p1]<B[p2]:
                re.append(A[p1])
                p1+=1
            else:
                re.append(B[p2])
                p2+=1
        if p1==len(A):
            re.extend(B[p2:])
        if p2 == len(B):
            re.extend(A[p2:])
        return re


if __name__ == '__main__':
    s =Solution()
    A=[1,2,3]
    B=[1,2,3]
    print s.mergeSortedArray(A, B)
