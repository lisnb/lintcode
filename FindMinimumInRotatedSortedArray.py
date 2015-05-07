#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: lisnb
# @Date:   2015-04-28 23:41:34
# @Last Modified by:   lisnb
# @Last Modified time: 2015-04-29 23:53:04


class Solution:
    # @param num: a rotated sorted array
    # @return: the minimum number in the array
    def findMin(self, num):
        # write your code here
        if not num:
            return -1
        # i = len(num)-1
        # while i>=0 and num[i]==num[0]:
        #     i-=1
        return self.findmin(num, 0, len(num)-1)
    
    def findmin(self, num, b, e):
        print b, e
        if b==e:
            return num[b]
        if b+1 == e:
            return min(num[b], num[e])
        mid = b+(e-b)/2
        print b, e, mid, num[mid],num[b],num[e],num[mid]<num[mid+1] and num[mid]<num[mid-1]
        if num[mid]<num[mid+1] and num[mid]<num[mid-1]:
            return num[mid]
        if num[mid] == num[e]:
            lm = self.findmin(num, b, mid-1)
            rm = self.findmin(num, mid+1, e)
            return min(lm,rm)
        if num[mid]>num[e]:
            return self.findmin(num, mid+1,e)
        else:
            return self.findmin(num, b, mid-1)

if __name__ == '__main__':
    s = Solution()
    # num = [3,2,1,2,2,2,2,2,2,3,3,3,3,3]
    # num = [2,1,2,2,2,2,2,2,2]
    # num = [3,1]
    num = [1,1,1,1,1,1,-1,1]
    print s.findMin(num)

