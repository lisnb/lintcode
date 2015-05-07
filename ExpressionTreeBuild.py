#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: LiSnB
# @Date:   2015-05-06 21:04:23
# @Last Modified by:   LiSnB
# @Last Modified time: 2015-05-07 08:46:34


"""
Definition of ExpressionTreeNode:
"""
class ExpressionTreeNode:
    def __init__(self, symbol):
        self.symbol = symbol
        self.left, self.right = None, None



class Solution:
    # @param expression: A string list
    # @return: The root of expression tree
    operset = set(['(',')','+','-','*','/'])
    operprio = {
        '+':1,
        '-':1,
        '*':2,
        '/':2
    }
    def convertToList(self, expression):
        expres = []
        i, j=0, 0 
        while j<len(expression):
            if expression[j] in Solution.operset:
                if i<j:
                    expres.append(expression[i:j])
                expres.append(expression[j])
                i = j+1
                j = j+1
            else:
                j+=1
        if i<j:
            expres.append(expression[i:j])
        return expres

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

    def build(self, expression):
        # expression = self.convertToList(expression)
        print expression
        return self.buildtree(expression, 0, len(expression)-1)

    def buildtree(self, expression, b, e):
        print b, e
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
        # inparenthesis = False
        weight = 1
        parentheses = []
        for i in range(b, e+1):
            if expression[i] == '(':
                parentheses.append(1)
                # inparenthesis = True
                # weight=10
                continue
            if expression[i] == ')':
                # if parentheses[-1]==1:
                parentheses.pop()
                # inparenthesis = False
                # weight=1
                continue
            # print 'weight', weight
            # if not inparenthesis:
            if len(parentheses)==0:
                tprio = weight*Solution.operprio.get(expression[i], 100)
                # print i, expression[i], tprio
                if tprio<=lowestprio:
                    lowestprio = tprio
                    lowestoper = i
        print 'operator', expression[lowestoper], lowestoper
        root = ExpressionTreeNode(expression[lowestoper])
        root.left = self.buildtree(expression, b, lowestoper-1)
        root.right = self.buildtree(expression, lowestoper+1, e)
        return root


if __name__ == '__main__':
    # expression = '(23+7)/(1+2)'
    # expression = '(23+7)+7'
    expression = '(2*6-(23+7)/(1+2))'
    # expression = ["(","(","(","(","(",")",")",")",")",")"]
    # expression = ["2","*","6","-","(","23","+","7",")","/","(","1","+","2",")"]
    # expression = ["(","(","999","/","499","*","(","396","/","(","3","+","3","+","3",")","-","5",")",")","/","6","-","1","/","1",")","/","3"]
    print ''.join(expression)
    # exit()
    s = Solution()
    print s.build(expression)
    # print s.islegal('((((())', 0, 6)



