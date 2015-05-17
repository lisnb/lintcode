#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: lisnb
# @Date:   2015-05-08 22:55:15
# @Last Modified by:   lisnb
# @Last Modified time: 2015-05-08 23:05:28


class Solution:
    # @param num :  a list of integer
    # @return : a list of integer
    def nextPermutation(self, num):
        # write your code here
        
        if not num or len(num)==1:
        	return num 
        i = 0
        for j in range(1, len(num)):
        	if num[j-1]<num[j]:
        		i = j
        if i==0:
        	num.reverse()
        	return num

        pi1 = num[i-1]

        h = 0
        for k in range(0, len(num)):
        	if pi1<num[k]:
        		h = k 

        num[i-1], num[h] = num[h], num[i-1]
        num2 = num[i:]
        num2.reverse()
        num1 = num[0:i]
        num1.extend(num2)
        return num1

if __name__ == '__main__':
	num = [4,3,2,1]
	s = Solution()
	print s.nextPermutation(num)

