#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: lisnb
# @Date:   2015-04-30 00:04:24
# @Last Modified by:   lisnb
# @Last Modified time: 2015-05-01 09:56:10
import time

class Solution:
    """
    @param L: Given n pieces of wood with length L[i]
    @param k: An integer
    return: The maximum length of the small pieces.
    """
    def woodCut(self, L, k):
        # write your code here
        if not L or sum(L)<k:
            return 0
        if sum(L)==k:
            return 1 
        ml = max(L)
        b = ml
        print b
        while b>0:
            print [l/b for l in L]
            n = sum(l/b for l in L)
            print n
            if n>=k:
                break#return b 
            b/=2
        if b==0:
            return 0
        print b
        while b<ml:
            time.sleep(0.2)
            print b, ml
            if ml-b==1:
                return ml if sum(l/ml for l in L)>=k else b
            mid = b+(ml-b)/2
            n = sum(l/mid for l in L)
            print b, ml, mid, [l/mid for l in L]
            if n>=k:
                b = mid
            else:
                ml = mid-1
        return b


if __name__ == '__main__':
    # L = [232, 124, 456]
    L = [2147483644,2147483645,2147483646,2147483647]
    s = Solution()
    print s.woodCut(L, 4)