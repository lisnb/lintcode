#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: LiSnB
# @Date:   2015-04-28 20:57:02
# @Last Modified by:   LiSnB
# @Last Modified time: 2015-04-28 22:37:34


class Solution:
    """
    @param A : a list of integers
    @param target : an integer to be searched
    @return : an integer
    """
    def search(self, A, target):
        # write your code here
        return self.binarysearch(A, target, 0, len(A)-1)


    def binarysearch(self, A, target, b, e):
        if e<b:
            return -1
        if e==b:
            return b if A[b]==target else -1

        mid = b + (e-b)/2

        if A[mid]==target:
            return mid
        if A[b]<A[e]:
            if A[mid] > target:
                return self.binarysearch(A, target, b, mid -1)
            else:
                return self.binarysearch(A, target, mid+1, e)
        else:
            if target == A[b]:
                return b
            if target == A[e]:
                return e 
            if A[mid]>A[b]:
                if target>A[mid]:
                    return self.binarysearch(A, target, mid+1,e-1)
                else:
                    if target>A[b]:
                        return self.binarysearch(A, target, b+1, mid-1)
                    else:
                        return self.binarysearch(A, target, mid+1, e-1)
            else:
                if target<A[mid]:
                    return self.binarysearch(A, target, b+1, mid-1)
                else:
                    if target>A[e]:
                        return self.binarysearch(A, target, b+1, mid-1)
                    else:
                        return self.binarysearch(A, target, mid+1, e-1)





if __name__ == '__main__':
    s = Solution()

    A = [7,8,1,2,3,4,5,6, 7,7,7,7]

    for i in range(1, 10):
        print i, s.search(A, i)