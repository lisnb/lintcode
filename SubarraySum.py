#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: LiSnB
# @Date:   2015-04-26 13:36:05
# @Last Modified by:   LiSnB
# @Last Modified time: 2015-04-26 14:01:08


class Solution:
    """
    @param nums: A list of integers
    @return: A list of integers includes the index of the first number 
             and the index of the last number
    """
    def subarraySum(self, nums):
        # write your code here
        dic = {0:[-1]}
        s = 0
        re = []
        for i, num in enumerate(nums):
            s+=num
            if num == 0:
                re.append([i,i])
                continue
            if s in dic:
                # return [dic[s][0]+1, i]
                re.extend([[x+1, i] for x in dic[s]])
            else:
                dic[s]=[]
            dic[s].append(i)
        print dic
        return re

    def subarraySum2(self, nums):
        # write your code here
        dic = {0:-1}
        s = 0
        re = []
        for i, num in enumerate(nums):
            s+=num
            if num == 0:
                return [i,i]
            if s in dic:
                return [dic[s]+1, i]
            else:
                dic[s]=i
        return re

if __name__ == '__main__':
    s = Solution()
    # print s.subarraySum2([0])
    print s.subarraySum2([-3,1,2,1,-3,4,1,-1,2,-4,-3,-4,5,-1])