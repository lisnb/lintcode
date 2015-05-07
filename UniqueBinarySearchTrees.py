#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: lisnb
# @Date:   2015-05-04 23:09:51
# @Last Modified by:   lisnb
# @Last Modified time: 2015-05-04 23:16:57

class Solution:
    # @paramn n: An integer
    # @return: An integer
    def numTrees(self, n):
        # write your code here
        caches=[1,1,2,5]
        if n==0:
            return 0
        for i in range(4,n+1):
            j = i/2
            cnt = 0
            for k in range(1, j+1):
                cnt+=(caches[k-1]*caches[i-k])
            cnt*=2
            if i%2 == 1:
                cnt+=caches[j]*caches[j]
            caches.append(cnt)
        return caches[n]

            
if __name__ == '__main__':
	s = Solution()
	print s.numTrees(7)