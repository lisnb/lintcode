#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: lisnb
# @Date:   2015-05-07 22:48:54
# @Last Modified by:   lisnb
# @Last Modified time: 2015-05-07 22:50:06


class Solution:	
    #@param num: A list of non negative integers
    #@return: A string
    def largestNumber(self, num):
        # write your code here
        if not num:
            return 0
        num = [str(n) for n in num]
        num.sort(cmp = lambda x, y: cmp(y+x, x+y))
        return ''.join(num)

if __name__ == '__main__':
	nums = [1,20,23,4,8]
	s = Solution()
	print s.largestNumber(nums)