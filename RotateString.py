#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: lisnb
# @Date:   2015-05-07 18:49:39
# @Last Modified by:   lisnb
# @Last Modified time: 2015-05-07 18:50:58


class Solution:
    """
    param A: A string
    param offset: Rotate string with offset.
    return: Rotated string.
    """
    def rotateString(self, A, offset):
        # write you code here
        a = list(A)
        offset %= len(a)
        if offset == 0:
            return A
        l1 = a[:len(a)-offset]
        l2 = a[len(a)-offset:]
        l2.extend(l1)
        return ''.join(l2)

if __name__ == '__main__':
	s = Solution()
	A= 'abcdefg'
	for i in range(0, 10):
		print s.rotateString(A, i)
