#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: lisnb
# @Date:   2015-05-07 22:24:40
# @Last Modified by:   lisnb
# @Last Modified time: 2015-05-07 22:48:48
import random

class Solution:
    """
    @param nums: A list of integers
    @return: The majority number
    """
    def majorityNumber(self, nums):
        # write your code here
        

if __name__ == '__main__':
	nums = [1,1,1,1,2,2,2,3,3,3]
	random.shuffle(nums)
	print nums
	s = Solution()
	print s.majorityNumber(nums)

