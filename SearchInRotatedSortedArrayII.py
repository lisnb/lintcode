#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: lisnb
# @Date:   2015-04-28 23:39:09
# @Last Modified by:   lisnb
# @Last Modified time: 2015-04-28 23:40:07
class Solution:
    """
    @param A : an integer ratated sorted array and duplicates are allowed
    @param target : an integer to be searched
    @return : a boolean
    """
    def search(self, A, target):
        return self.binarysearch(A, target, 0, len(A)-1)


    def binarysearch(self, A, target, b, e):
        if e<b:
            return False
        if e==b:
            return  A[b]==target

        mid = b + (e-b)/2

        if A[mid]==target:
            return True
        if A[b]<A[e]:
            if A[mid] > target:
                return self.binarysearch(A, target, b, mid -1)
            else:
                return self.binarysearch(A, target, mid+1, e)
        else:
            if target == A[b]:
                return True
            if target == A[e]:
                return True 
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

    A = [7,8,1,2,3,4,5,6,7,7,7,7]

    for i in range(1, 10):
        print i, s.search(A, i)
