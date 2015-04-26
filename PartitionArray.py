#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: LiSnB
# @Date:   2015-04-26 15:39:33
# @Last Modified by:   LiSnB
# @Last Modified time: 2015-04-26 15:58:36


class Solution:
    """
    @param nums: The integer array you should partition
    @param k: As description
    @return: The index after partition
    """
    def partitionArray(self, nums, k):
        # write your code here
        # you should partition the nums by k
        # and return the partition index as description

        if not nums:
            return 0
        p1, p2 = -1, 0
        while p2<len(nums):
            if nums[p2]<k:
                p1+=1
                nums[p1], nums[p2] = nums[p2], nums[p1]
            p2+=1
        return p1+1

if __name__ == '__main__':
    s = Solution()
    nums = [3,2,2,1,5,6,7,8,1]
    print s.partitionArray(nums, 9)
    print nums