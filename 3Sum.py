#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: LiSnB
# @Date:   2015-04-26 16:21:41
# @Last Modified by:   LiSnB
# @Last Modified time: 2015-04-26 16:50:16


class Solution:
    """
    @param numbersbers : Give an array numbersbers of n integer
    @return : Find all unique triplets in the array which gives the sum of zero.
    """
    def threeSum(self, numbers):
        # write your code here
        if not numbers:
            return []
        numbers.sort()
        re = []
        b = 0
        while b<len(numbers)-2:
            self.twosum(numbers, 0-numbers[b], b+1, re)
            while b+1<len(numbers)-2 and numbers[b]==numbers[b+1]:
                b+=1
            b+=1
        return re

    def twosum(self, numbers, target, b, re):
        bb, ee, cur = b, len(numbers)-1, numbers[b-1]
        while bb<ee:
            cs = numbers[bb]+numbers[ee]
            if cs == target:
                re.append((cur, numbers[bb], numbers[ee]))
                while bb+1<ee and numbers[bb]==numbers[bb+1]:
                    bb+=1
                while ee-1>bb and numbers[ee]==numbers[ee-1]:
                    ee-=1
                bb+=1
                ee-=1
            elif cs>target:
                ee-=1
            else:
                bb+=1

if __name__ == '__main__':
    s = Solution()
    nums = [1,0,-1,-1,-1,-1,0,1,1,1]
    print s.threeSum(nums)
