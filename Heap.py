#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: lisnb
# @Date:   2015-05-15 11:43:14
# @Last Modified by:   lisnb
# @Last Modified time: 2015-05-15 20:41:37




def adjust(array, i, ll):

    # ll = len(array)
    # ti = i
    while i<ll:
        ti = i
        l, r = i*2+1, i*2+2
        
        if l<ll and array[l]>array[i]:
            i = l 
        if r<ll and array[r]>array[i]:
            i = r
        if ti != i:
            array[ti], array[i] = array[i], array[ti]
        else:
            break
        # adjust(array, ti, ll)

def makeheap(array):
    ll = len(array)
    i = ll/2-1
    while i>=0:
        adjust(array, i, ll)
        i-=1


def heapsort(array):
    makeheap(array)
    # print array
    ll = len(array)
    for i in range(len(array)-1, 0, -1):
        array[i], array[0] = array[0],array[i]
        # print array, i
        adjust(array, 0, i)
        # print array

def insert(array, n):
    array.append(n)
    i = len(array)-1
    while i>0:
        if array[(i-1)/2]<n:
            array[i] = array[(i-1)/2]
            i = (i-1)/2
        else:
            break
    array[i] = n

def insert2(array, n):
    array.append(n)
    i = len(array)-1
    while i>0 and array[(i-1)/2]<n:
        array[i] = array[(i-1)/2]
        i=(i-1)/2
    array[i] = n




if __name__ == '__main__':
    import random
    # array = [random.randint(1,100) for x in range(40)]
    array=[0]
    # array = range(1,11)
    # array = [27, 59, 4, 29]
    # array = 
    print array
    makeheap(array)
    # heapsort(array)

    # insert2(array, 30)
    print array
    # makeheap(array)
    heapsort(array)

    print array


        