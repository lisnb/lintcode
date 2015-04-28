#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: LiSnB
# @Date:   2015-04-28 20:02:49
# @Last Modified by:   LiSnB
# @Last Modified time: 2015-04-28 20:17:50



class Solution:
    # @param nums: The integer array
    # @param target: Target number to find
    # @return the first position of target in nums, position start from 0 
    def binarySearch(self, nums, target):
        # write your code here
        if not nums:
            return -1
        return self.binarysearch(nums, target, 0, len(nums)-1)

    def binarysearch(self, nums, target, b, e):
        if b>e:
            return -1
        if b==e :
            return -1 if nums[b] != target else b 
        mid = b + (e-b)/2
        if nums[mid] == target:
            if mid-1>=0 and nums[mid-1]==target:
                return self.binarysearch(nums, target, b, mid-1)
            # while mid-1>=0 and nums[mid-1]==target:
            #     mid-=1
            else:
                return mid 
        if nums[mid]>target:
            return self.binarysearch(nums, target, b, mid-1)
        else:
            return self.binarysearch(nums, target, mid+1, e)

if __name__ == '__main__':
    s = Solution()
    nums = [1, 2, 3, 3,3, 4, 5,5,5,10]
    print s.binarySearch(nums, 3)