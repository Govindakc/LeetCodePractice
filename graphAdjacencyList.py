#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Graph representation using Adjacency List

Created on Thu Apr  5 06:20:01 2020
@author: Govinda KC

"""

import collections
class Graph:
    def __init__(self, nodes, graph_list=collections.defaultdict(list), is_directed = False):
        self.nodes = nodes
        self.graph_list = graph_list
        self.is_directed = is_directed
        
    def addEdges(self):
        for u,v in self.nodes:
            self.graph_list[u].append(v)
            
            # This will be implemented if not directed.
            if not self.is_directed:
                self.graph_list[v].append(u)
        
    def printGraph(self):
        for i in self.graph_list:
            print(str(i)+'------->'+ str(self.graph_list[i]))
        
if __name__ == '__main__':
    
    L = [(1,2), (3,4), (1,3), (4,5), (4,2)]
    # For directed graph: is_directed=True
    gp = Graph(L, is_directed=False)
    gp.addEdges()
    gp.printGraph()
