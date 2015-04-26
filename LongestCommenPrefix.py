#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: lisnb
# @Date:   2015-04-26 11:28:23
# @Last Modified by:   lisnb
# @Last Modified time: 2015-04-26 11:31:29

class Solution:
    # @param A, B: Two string.
    # @return: the length of the longest common substring.
    def longestCommonSubstring(self, A, B):
        # write your code here
        
        if not A or not B:
            return ''
        map = [[0]*len(A) for b in B]
        
        for i in range(len(A)):
            if A[i]==B[0]:
                map[0][i]=1
        for j in range(1,len(B)):
            if A[0]==B[j]:
                map[j][0]=1
        
        for i in range(1,len(B)):
            for j in range(1,len(A)):
                if B[i]==A[j]:
                    map[i][j]=map[i-1][j-1]+1            
        return max([max(m) for m in map])

if __name__ == '__main__':
    s = Solution()
    a = 'www.lintcode.com code'
    b = 'www.ninechapter.com code'
    print s.longestCommonSubstring(a,b)
