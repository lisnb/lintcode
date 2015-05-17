#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: lisnb
# @Date:   2015-05-08 22:40:41
# @Last Modified by:   lisnb
# @Last Modified time: 2015-05-08 22:51:20



class Solution:
    # @param A, a list of integers
    # @return a boolean
    def canJump(self, A):
        # write your code here
        if not A:
            return True
        i = 0
        maxstep = 0
        end = len(A)-1
        while i<=maxstep:
            if maxstep>=end:
                return True
            if A[i]+i>maxstep:
                maxstep = A[i]+i
            i+=1
        return False


if __name__ == '__main__':
    A = [2]

    B = [3,2,1,0,4]

    s = Solution()

    print s.canJump(A)
    print s.canJump(B)



