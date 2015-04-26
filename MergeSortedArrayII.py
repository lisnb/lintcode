#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: LiSnB
# @Date:   2015-04-26 14:42:31
# @Last Modified by:   LiSnB
# @Last Modified time: 2015-04-26 15:03:48


class Solution:
    """
    @param A: sorted integer array A which has m elements, 
              but size of A is m+n
    @param B: sorted integer array B which has n elements
    @return: void
    """
    def mergeSortedArray(self, A, m, B, n):
        # write your code here
        i = m+n-1
        ia, ib = m-1, n-1
        if n==0:
            return
        if m==0:
            A[:]=B
            return 
        while ia >= 0 and ib >=0:
            if A[ia]>B[ib]:
                A[i]=A[ia]
                ia-=1
            else:
                A[i]=B[ib]
                ib-=1
            i-=1

        if ia<0:
            A[:ib+1] = B[:ib+1]


if __name__ == '__main__':
    s = Solution()
    A = [4,5,6, None, None]
    B = [1,2]
    s.mergeSortedArray(A, 3, B, 2)
    print A                

