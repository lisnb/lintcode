#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: lisnb
# @Date:   2015-05-07 18:52:03
# @Last Modified by:   lisnb
# @Last Modified time: 2015-05-07 19:02:37




class Solution:
    """
    @param nums: A list of integers
    @return: An integer denote the sum of maximum subarray
    """
    def maxSubArray(self, nums):
        # write your code here
		tmax = -0xFFFFFFFF
		tsum = 0

		for num in nums:
			tsum +=  num
			if tsum>tmax:
				tmax = tsum
			if tsum < 0:
				tsum = 0
		return tmax

if __name__ == '__main__':
	nums = [ -2,2,-3,4,-1,2,1,-5,3 ]
	s = Solution()
	print s.maxSubArray(nums)