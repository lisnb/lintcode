#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: lisnb
# @Date:   2015-05-07 22:24:40
# @Last Modified by:   lisnb
# @Last Modified time: 2015-05-07 22:24:55


class Solution:
    """
    @param nums: A list of integers
    @return: The majority number
    """
    def majorityNumber(self, nums):
        # write your code here
        maj, cnt = nums[0], 0
        for num in nums:
            if cnt == 0:
                maj = num
                cnt+=1
            elif num == maj:
                cnt+=1
            else:
                cnt-=1
                
        return maj