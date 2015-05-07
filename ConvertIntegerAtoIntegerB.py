#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: lisnb
# @Date:   2015-05-02 10:44:33
# @Last Modified by:   lisnb
# @Last Modified time: 2015-05-02 11:15:44
import time
class Solution:
    """
    @param a, b: Two integer
    return: An integer
    """
    def bitSwapRequired(self, a, b):
        # write your code here
        c = a^b 
        cnt = 0
        print bin(a), bin(b), bin(c)
        if c<0:
            cnt+=1
            c&=((1<<31)-1)
        while c!=0:
            time.sleep(0.1)
            print bin(c)
            cnt += c&1
            c>>=1
        return cnt 

if __name__ == '__main__':
    s = Solution()
    print s.bitSwapRequired(1,-2)
