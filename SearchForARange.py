#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: lisnb
# @Date:   2015-05-01 10:15:19
# @Last Modified by:   lisnb
# @Last Modified time: 2015-05-02 10:36:22


class Solution:
    """
    @param A : a list of integers
    @param target : an integer to be searched
    @return : a list of length 2, [index1, index2]
    """
    def searchRange(self, A, target):
        # write your code here
        if not A:
            return [-1,-1]
        if len(A) == 1:
            return [-1,-1] if A[0]!=target else [0,0]
        tmin, tmax = self.search(A, target, 0, len(A)-1)
        return [tmin, tmax]

    def search(self, A, target, b, e):
        if b==e:
            if A[b]==target:
                return b, b
            else:
                return -1, -1
        if b>e:
            return -1, -1
        mid = b+(e-b)/2
        if A[mid]>target:
            return self.search(A, target, b, mid-1)
        elif A[mid]<target:
            return self.search(A, target, mid+1, e)
        else:
            lmin, lmax = self.search(A, target, b, mid-1)
            rmin, rmax = self.search(A, target, mid+1, e)
            tmin = mid if lmin == -1 else lmin
            tmax = mid if rmax == -1 else rmax
            return tmin, tmax

if __name__ == '__main__':
    s = Solution()
    A = [5,5,7,7,8,8,8,8,8,8,8,10]
    print s.searchRange(A[0:2], 5)
