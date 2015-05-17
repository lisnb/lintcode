#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: lisnb
# @Date:   2015-05-17 00:45:16
# @Last Modified by:   lisnb
# @Last Modified time: 2015-05-17 10:59:22



# Definition for a Directed graph node
# class DirectedGraphNode:
#     def __init__(self, x):
#         self.label = x
#         self.neighbors = []

class Solution:
    """
    @param graph: A list of Directed graph node
    @param s: the starting Directed graph node
    @param t: the terminal Directed graph node
    @return: a boolean value
    """
    def hasRoute(self, graph, s, t):
        # write your code here
        if not graph:
            return False
        flags = {x.label:0 for x in graph}
        return self.dfs(s, t, flags)

    def dfs(self, s, t, flags):
        flags[s.label] = 1
        if s.label == t.label:
            flags[s.label] = 2
            return True
        for neighbor in s.neighbors:
            if flags[neighbor.label] == 1:
                return False
            if flags[neighbor.label] == 0:
                tmd = self.dfs(neighbor, t, flags)
                if tmd:
                    return True
        flags[s.label] = 2
        return False

    def hasRouteBFS(self, graph, s, t):
        import Queue
        flags = {x.label: 0 for x in graph}

    def bfs(self, s, t, flags):

        q = Queue.Queue()
        q.put(s)
        flags[s.label] = 1
        if s.label == t.label:
            return True
        while not q.empty():
            th = q.get()
            for neighbor in th.neighbors:
                if flags[neighbor.label] == 1:
                    continue
                if neighbor.label == t.label:
                    return True
                q.put(neighbor)
                flags[neighbor.label] = 1

        return False





