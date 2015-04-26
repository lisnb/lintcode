#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: lisnb
# @Date:   2015-04-26 11:37:55
# @Last Modified by:   lisnb
# @Last Modified time: 2015-04-26 11:43:23



class Solution:
    """
    @param A: A list of integers
    @param elem: An integer
    @return: The new length after remove
    """
    def removeElement(self, A, elem):
        # write your code here
        
        if not A :
            return 0 
        p1, p2 = -1, 0
        while p2<len(A):
            if A[p2]!=elem:
                p1+=1
                A[p1], A[p2] = A[p2], A[p1]
            p2+=1

        return p1+1

if __name__ == '__main__':
    s = Solution()
    e = [0,4,4,0,0,2,4,4]
    print s.removeElement(e, 3)
    print e
