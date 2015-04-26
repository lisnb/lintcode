#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: LiSnB
# @Date:   2015-04-26 15:59:12
# @Last Modified by:   LiSnB
# @Last Modified time: 2015-04-26 16:20:39


class Solution:
    """
    @param numbers : An array of Integer
    @param target : target = numbers[index1] + numbers[index2]
    @return : [index1 + 1, index2 + 1] (index1 < index2)
    """
    def twoSum(self, numbers, target):
        # write your code here
        if not numbers or len(numbers)<2:
            return [-1, -1]
        dic = {}
        for i, number in enumerate(numbers):
            if number not in dic:
                dic[number] = []
            dic[number].append(i)

        numbers.sort()
        p1, p2 = 0, len(numbers)-1
        while p1<p2:
            cs = numbers[p1]+numbers[p2]
            if cs == target:
                # return [p1+1, p2+1]
                break 
            elif cs>target:
                p2-=1
            else:
                p1+=1
        if p1>=p2:
            return [-1, -1]
        else:
            if numbers[p1]==numbers[p2]:
                return [min(dic[numbers[p1]])+1, max(dic[numbers[p1]])+1]
            else:
                return [min(dic[numbers[p1]][0],dic[numbers[p2]][0])+1,max(dic[numbers[p1]][0],dic[numbers[p2]][0])+1]

        # return [-1, -1]

    # def twoSum(self, numbers, target):


if __name__ == '__main__':
    s = Solution()
    numbers = [1, 0, -1]
    print s.twoSum(numbers, -1)


