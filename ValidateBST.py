#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: lisnb
# @Date:   2015-04-25 23:18:44
# @Last Modified by:   lisnb
# @Last Modified time: 2015-04-25 23:40:43
class Node(object):
    """docstring for Node"""
    def __init__(self, val):
        super(Node, self).__init__()
        self.val = val
        self.left = None
        self.right = None


def valid(root):
    if not root:
        return False, None, None
    if not root.left and not root.right:
        return True, root.val, root.val 
    if not root.left:
        r, rmax, rmin = valid(root.right)
        if not r or rmin<=root.val:
            return False, None, None
        return True, rmax, root.val
    if not root.right:
        r, lmax, lmin = valid(root.left)
        if not r or lmax>=root.val:
            return False, None, None
        return True, root.val, lmin
    rr, rmax, rmin = valid(root.right)
    rl, lmax, lmin = valid(root.left)
    return rr and rl and lmax<root.val<rmin, lmin, rmax 


if __name__ == '__main__':
    n1 = Node(1)
    n2 = Node(2)
    n3 = Node(3)
    n2.left = n1
    n2.right = n3
    n4 = Node(4)
    n5 = Node(-1)
    n1.left = n5
    n3.right = n4
    print valid(n5)
