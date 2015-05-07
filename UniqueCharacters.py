#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: lisnb
# @Date:   2015-05-07 18:12:09
# @Last Modified by:   lisnb
# @Last Modified time: 2015-05-07 18:13:13



class Solution:
    # @param s: a string
    # @return: a boolean
    def isUnique(self, stri):
        # write your code here
        if not stri:
            return True
        flags = [False]*256
        for char in stri:
            t = ord(char)
            if flags[t]:
                return False
            flags[t]=True
        return True


if __name__ == '__main__':
	s = Solution()
	st = 'abb'
	print s.isUnique(st)