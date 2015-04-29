#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: LiSnB
# @Date:   2015-04-29 09:16:33
# @Last Modified by:   LiSnB
# @Last Modified time: 2015-04-29 09:26:02

class VersionControl:
   @classmethod
   def isBadVersion(cls, gid):
        return gid>2
# Run unit tests to check whether verison `id` is a bad version
#        # return true if unit tests passed else false.
# You can use VersionControl.isBadVersion(10) to check whether version 10 is a 
# bad version.
class Solution:
    """
    @param n: An integers.
    @return: An integer which is the first bad version.
    """
    def findFirstBadVersion(self, n):
        # write your code here
        return self.find(1, n)

    def find(self, b, e):
        if b>e:
            return -1
        if b==e:
            return b if VersionControl.isBadVersion(b) else -1
        if e-b==1:
            return b if VersionControl.isBadVersion(b) else e 
        mid = b+(e-b)/2
        if not VersionControl.isBadVersion(mid):
            return self.find(mid+1, e)
        else:
            if not VersionControl.isBadVersion(mid-1):
                return mid 
            else:
                return self.find(b, mid-1)


if __name__ == '__main__':
    s = Solution()
    print s.findFirstBadVersion(31)