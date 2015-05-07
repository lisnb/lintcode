#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: lisnb
# @Date:   2015-05-07 18:33:54
# @Last Modified by:   lisnb
# @Last Modified time: 2015-05-07 18:41:37





class Solution:
    """
    @param key: A String you should hash
    @param HASH_SIZE: An integer
    @return an integer
    """
    def hashCode(self, key, HASH_SIZE):
        # write your code here
        if not key:
        	return 0
        # index = len(key)-2
        hashkey = 33%HASH_SIZE
        tkey = hashkey
        tsum = ord(key[-1])
        for i in range(len(key)-2, -1, -1):
        	tsum += (tkey*ord(key[i])%HASH_SIZE)
        	tsum %= HASH_SIZE
        	tkey*=hashkey
        	tkey%=HASH_SIZE

        return tsum%HASH_SIZE


if __name__ == '__main__':
	key = 'abcd'
	s = Solution()
	print s.hashCode(key, 100)


