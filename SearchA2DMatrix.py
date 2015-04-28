#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: LiSnB
# @Date:   2015-04-28 20:10:17
# @Last Modified by:   LiSnB
# @Last Modified time: 2015-04-28 20:43:20

class Solution:
    """
    @param matrix, a list of lists of integers
    @param target, an integer
    @return a boolean, indicate whether matrix contains target
    """
    def searchMatrix(self, matrix, target):
        # write your code here
        if not matrix:
            return False
        rn = len(matrix)
        cn = len(matrix[0])
        r1 = self.searchandinsert(matrix, target, 0, 0, rn-1)
        if r1[0]:
            return True
        else:
            return self.binarysearch(matrix[r1[1]-1],target, 0, cn-1)


    def searchandinsert(self, matrix, target, col, b, e):
        if matrix[b][col]>target:
            return False, b
        if matrix[e][col]<target:
            return False, e+1
        mid = b + (e-b)/2
        if matrix[mid][col] == target:
            return True, mid 
        if matrix[mid][col]>target:
            return self.searchandinsert(matrix, target, col, b, mid-1)
        else:
            return self.searchandinsert(matrix, target, col, mid+1, e)

    def binarysearch(self, nums, target, b, e):
        if b>e:
            return False
        if b==e :
            return nums[b] == target
        mid = b + (e-b)/2
        if nums[mid] == target:
            if mid-1>=0 and nums[mid-1]==target:
                return self.binarysearch(nums, target, b, mid-1)
            else:
                return True 
        if nums[mid]>target:
            return self.binarysearch(nums, target, b, mid-1)
        else:
            return self.binarysearch(nums, target, mid+1, e)

if __name__ == '__main__':
    s = Solution()
    matrix = [
        [1, 3, 5, 7],
        [10, 11, 16, 20],
        [23, 30, 34, 50]
    ]
    for i in range(50):
        print i, s.searchMatrix(matrix[0:1], i)