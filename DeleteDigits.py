#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: lisnb
# @Date:   2015-05-07 22:59:04
# @Last Modified by:   lisnb
# @Last Modified time: 2015-05-10 01:37:05



class Solution:
    """
    @param A: A positive integer which has N digits, A is a string.
    @param k: Remove k digits.
    @return: A string
    """

    def DeleteDigits(self, A, k):
        stack = []
        popcnt = 0
        i = 0
        while i<len(A):
            if not stack:
                stack.append(A[i])
                i+=1
            elif A[i] >= stack[-1]:
                stack.append(A[i])
                i+=1
            else:
                if popcnt<k:
                    stack.pop()
                    popcnt += 1
                else:
                    stack.append(A[i])
                    i+=1

        if len(stack)>len(A)-k:
            stack = stack[:len(A)-k]
        i = 0
        while i<len(stack) and stack[i]=='0':
            i+=1
        if i == len(stack):
            return '0'
        else:
            return ''.join(stack[i:])



if __name__ == '__main__':
    s = Solution()
    A = '8000076543'
    print s.DeleteDigits(A, 7)

 
