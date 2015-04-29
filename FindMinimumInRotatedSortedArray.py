#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: lisnb
# @Date:   2015-04-28 23:41:34
# @Last Modified by:   lisnb
# @Last Modified time: 2015-04-29 00:01:33


class Solution:
    # @param num: a rotated sorted array
    # @return: the minimum number in the array
    def findMin(self, num):
        # write your code here
        if not num:
            return -1
        return self.findmin(num, 0, len(num)-1)
    
    def findmin(self, num, b, e):
        if b==e:
            return num[b]
        mid = b+(e-b)/2
        # print b, e, mid, num[mid],num[b],num[e],num[b]<num[mid]<num[e]
        if num[mid]<num[mid+1] and num[mid]<=num[mid-1]:
            return num[mid]
        if num[mid]>num[e]:
            return self.findmin(num, mid+1,e)
        else:
            return self.findmin(num, b, mid-1)

if __name__ == '__main__':
    s = Solution()
    num = [7,0,1]
    print s.findMin(num)
