#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: lisnb
# @Date:   2015-04-26 23:51:08
# @Last Modified by:   lisnb
# @Last Modified time: 2015-04-27 23:54:26


class Solution:
    """
    @param x: An integer
    @return: The sqrt of x
    """
    def sqrt(self, x):
        # write your code here
        if x<=1:
            return x
        last = 0
        current = 1
        while current*current<=x:
            last = current
            current *= 2
        #print current, last
        while True:
            mid = (last+current)/2
            msq = mid*mid
            if mid == last or msq == x:
                return mid
            if msq>x:
                current = mid 
            else:
                last = mid 


if __name__ == '__main__':
    s = Solution()
    for i in range(100):
        print i, s.sqrt(i)
    print s.sqrt(102)
