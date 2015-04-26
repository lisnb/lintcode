#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: LiSnB
# @Date:   2015-04-26 18:58:20
# @Last Modified by:   LiSnB
# @Last Modified time: 2015-04-26 19:04:09


"""
Definition of Interval.

"""
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end



class Solution: 
    """
    @param A, queries: Given an integer array and an Interval list
                       The ith query is [queries[i-1].start, queries[i-1].end]
    @return: The result list
    """
    def intervalSum(self, A, queries):
        # write your code here
        if not A or not queries:
            return []
        sums = []
        s = 0
        for a in A:
            s+=a 
            sums.append(s)
        re = []
        for query in queries:
            if query[0] == 0:
                re.append(sums[query[1]])
            else:
                re.append(sums[query[1]]-sums[query[0]-1])
        return re

if __name__ == '__main__':
    s =  Solution()
    A = [1,2,7,8,5]
    queries = [(0,2), (0,4), (2,4)]
    print s.intervalSum(A, queries)
