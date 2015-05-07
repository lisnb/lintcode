#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: lisnb
# @Date:   2015-05-02 11:26:17
# @Last Modified by:   lisnb
# @Last Modified time: 2015-05-02 11:33:16


class Solution:
    """
    @param n and m: positive integer(1 <= n , m <= 100)
    @return an integer
    """ 
    def uniquePaths(self, m, n):
        # write your code here
        if not m or not n or (m==1 and n==1):
            return 0
        if m==1 or n==1:
            return 1
        path = [[0]*n for mm in range(m)]
        for i in range(n):
            path[0][i] = 1
        for i in range(m):
            path[i][0] = 1
        for i in range(1,m):
            for j in range(1,n):
                path[i][j] = path[i-1][j]+path[i][j-1]
        print path
        return path[m-1][n-1]

if __name__ == '__main__':
    s = Solution()
    print s.uniquePaths(2,2)



