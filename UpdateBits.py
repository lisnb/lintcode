#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: lisnb
# @Date:   2015-05-04 23:29:01
# @Last Modified by:   lisnb
# @Last Modified time: 2015-05-04 23:45:53


class Solution:
    #@param n, m: Two integer
    #@param i, j: Two bit positions
    #return: An integer
    def updateBits(self, n, m, i, j):
        # write your code here
		nn = list(bin(n&0xFFFFFFFF)[2:])
		mm = list(bin(m&0xFFFFFFFF)[2:])
		print nn, mm
		if i==0:
			nn[-(j+1):]=mm
		else:
			nn[-(j+1):-i]=mm
		print nn, len(nn)
		return int(''.join(nn), 2)

if __name__ == '__main__':
	s = Solution()
	# print bin(s.updateBits(int('10000000000',2), int('10101',2), 2,6))
	# r = s.updateBits(1024, 21, 0, 4)
	r = s.updateBits(1, -1, 0, 31)
	print r, bin(r)
