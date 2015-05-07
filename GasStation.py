#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: LiSnB
# @Date:   2015-05-05 08:59:47
# @Last Modified by:   LiSnB
# @Last Modified time: 2015-05-05 09:04:36


class Solution:
    # @param gas, a list of integers
    # @param cost, a list of integers
    # @return an integer
    def canCompleteCircuit(self, gas, cost):
        # write your code here
        if not gas or not cost:
            return -1
        tmin = 100
        loc = -1
        tsum = 0
        for i in range(0, len(gas)):
            tsum += (gas[i]-cost[i])
            if tsum<tmin:
                tmin = sum
                loc = i
        return -1 if tsum<0 else (loc+1)%len(gas)

if __name__ == '__main__':
    s = Solution()
    gas = [2,0,1,2,3,4,0]
    cost = [0,1,0,0,0,0,11]
    for i in range(0, len(gas)):
        print gas[i]-cost[i]
    print s.canCompleteCircuit(gas, cost)