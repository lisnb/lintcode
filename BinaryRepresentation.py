#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: lisnb
# @Date:   2015-05-02 23:43:41
# @Last Modified by:   lisnb
# @Last Modified time: 2015-05-03 01:17:11
import time

class Solution:
    #@param n: Given a decimal number that is passed in as a string
    #@return: A string
    def binaryRepresentation(self, n):
        # write you code here
        # import decimal
        n = float(n)
        neg = n<0
        zn = int(abs(n))
        fn = abs(n)-zn
        if neg:
            zn=-zn
        zs = bin(zn&0xFFFFFFFF)[2:]
        if fn==0:
            return zs 
        d = set()
        fs=[]
        while fn>1e-4:
            time.sleep(0.2)
            if abs(1-fn)<1e-3:
                fs.append('1')
                break
            t = int(fn*2)
            print fn, fn*2, t
            if t==1:
                fs.append('1')
            else:
                fs.append('0')
            fn = round(fn*2-t, 4)
            if fn in d:
                return 'ERROR'
            d.add(fn)
        fs = ''.join(fs)
        s = '%s.%s'%(zs,fs)
        return s

def binary_float2(x, n=100):
    from decimal import Decimal
    a = Decimal(x)*2

    r = []
    visited_set = set()
    visited_list = []
    for i in xrange(n):
        if a in visited_set:
            break
        visited_set.add(a)
        visited_list.append(a)
        if a >= 1:
            r.append("1")
            a -= 1
        else:
            r.append("0")
        a = a*2
    r.insert(visited_list.index(a), "[")
    return "0." + "".join(r) + "]"

if __name__ == '__main__':
    s = Solution()
    print s.binaryRepresentation('4096.6435546875')
    print s.binaryRepresentation('0.6418459415435791')
    print s.binaryRepresentation('17817287.6418609619140625')
    print s.binaryRepresentation('0.6418459415435791')
    print s.binaryRepresentation('28187281.128121212121')

    # print binary_float2(0.1)
