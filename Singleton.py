#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: LiSnB
# @Date:   2015-05-07 12:44:53
# @Last Modified by:   LiSnB
# @Last Modified time: 2015-05-07 12:49:41

class Solution:
    # @return: The same instance of this class every time
    cnt = 0
    instance = None
    def __init__(self):
        self.index = Solution.cnt
    @classmethod
    def getInstance(cls):
        # write your code here
        if Solution.cnt == 0:
            Solution.cnt = 1
            Solution.instance = Solution()
            return Solution.instance
        else:
            return Solution.instance

if __name__ == '__main__':
    s1 = Solution.getInstance()
    s2 = Solution.getInstance()
    print id(s1), id(s2)
    print s1.index, s2.index

