#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: lisnb
# @Date:   2015-04-26 22:38:07
# @Last Modified by:   lisnb
# @Last Modified time: 2015-04-26 22:53:06

class Solution:
    """
    @param A: a list of integers
    @return an integer
    """
    def removeDuplicates(self, A):
        # write your code here
        if not A:
            return 0
        cur = A[0]
        cnt = 1
        p = 1
        i = 1
        while p<len(A):
            if A[p] == cur:
                cnt+=1
            else:
                cur = A[p]
                cnt = 1
            if cnt<3:
                #122234444
                A[i]=A[p]
                i+=1
            p+=1
        return i



        

if __name__ == '__main__':
    s = Solution()  
    A = [1,1,1,2,2,2,5]
    print s.removeDuplicates(A)
    print A      
