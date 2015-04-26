#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: lisnb
# @Date:   2015-04-26 22:19:23
# @Last Modified by:   lisnb
# @Last Modified time: 2015-04-26 22:35:28


class Solution:
    """
    @param numbers: Give an array numbers of n integer
    @param target : An integer
    @return : return the sum of the three integers, the sum closest target.
    """
    def threeSumClosest(self, numbers, target):
        # write your code here
        if not numbers: 
            return None
        if len(numbers)<=3:
            return sum(numbers)
        numbers.sort()
        b = 0
        minsum = sum(numbers[:3])-target
        while b<len(numbers)-2:
            ntarget = target - numbers[b]
            tmin = self.twoSumClosest(numbers, ntarget, b+1)
            if tmin == 0:
                return target
            if abs(tmin)<abs(minsum):
                minsum = tmin
            while b+1<len(numbers)-2 and numbers[b]==numbers[b+1]:
                b+=1
            b+=1
        return minsum+target


    def twoSumClosest(self, numbers, target, b):
        bb, ee = b, len(numbers)-1
        minsum = sum(numbers[b:b+2])-target
        while bb<ee:
            tsum = numbers[bb]+numbers[ee]-target
            if tsum == 0:
                return 0
            elif tsum>0:
                ee-=1
            else:
                bb+=1

            if abs(tsum)<abs(minsum):
                minsum = tsum
        return minsum

            
if __name__ == '__main__':
    s = Solution()
    numbers = [-1, 2, 1, -4]
    print s.threeSumClosest(numbers,1)