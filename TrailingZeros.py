#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: lisnb
# @Date:   2015-05-02 11:35:35
# @Last Modified by:   lisnb
# @Last Modified time: 2015-05-02 12:08:50


class Solution:
    # @param n a integer
    # @return ans a integer
    def trailingZeros(self, n):
        
        cnt = 0
        while n>0:
            cnt+=n/5
            n/=5
        return cnt

if __name__ == '__main__':
    s = Solution()
    print s.trailingZeros(125)