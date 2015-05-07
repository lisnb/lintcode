#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: LiSnB
# @Date:   2015-05-07 09:00:52
# @Last Modified by:   LiSnB
# @Last Modified time: 2015-05-07 09:03:37


"""
Definition of ExpressionTreeNode:
"""
class ExpressionTreeNode:
    def __init__(self, symbol):
        self.symbol = symbol
        self.left, self.right = None, None

class Solution:
    # @param expression: A string list
    # @return: The Reverse Polish notation of this expression
    operset = set(['(',')','+','-','*','/'])
    operprio = {
        '+':1,
        '-':1,
        '*':2,
        '/':2
    }

    def islegal(self, expression, b, e):
        t = []
        for i in range(b, e+1):
            if expression[i]=='(':
                t.append(1)
                continue
            if expression[i]==')':
                if len(t)==0:
                    return False
                if t[-1]==1:
                    t.pop()
        return len(t)==0


    def buildtree(self, expression, b, e):
        while b<e and  expression[b]=='(' and expression[e]==')':
            if self.islegal(expression, b+1, e-1):
                b+=1
                e-=1
            else:
                break
        if b>e:
            return None
        if b==e:
            en = ExpressionTreeNode(expression[b])
            return en
        #find the last operator that has the lowest priority out of parentheses
        lowestprio = 100
        lowestoper = -1
        parentheses = []
        for i in range(b, e+1):
            if expression[i] == '(':
                parentheses.append(1)
                continue
            if expression[i] == ')':
                parentheses.pop()
                continue
            if len(parentheses)==0:
                tprio = Solution.operprio.get(expression[i], 100)
                if tprio<=lowestprio:
                    lowestprio = tprio
                    lowestoper = i
        root = ExpressionTreeNode(expression[lowestoper])
        root.left = self.buildtree(expression, b, lowestoper-1)
        root.right = self.buildtree(expression, lowestoper+1, e)
        return root

    def postordertraversal(self, root, r):
        if not root:
            return 
        self.postordertraversal(root.left, r)
        self.postordertraversal(root.right, r)
        r.append(root.symbol)

    def convertToRPN(self, expression):
        # write your code here
        root = self.buildtree(expression, 0, len(expression)-1)
        r = []
        self.postordertraversal(root, r)
        return r

if __name__ == '__main__':
    s = Solution()
    expression = ["3", "-", "4", "+", "5"]
    print s.convertToRPN(expression)
                    
