# #!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Graph representation using Adjacency Matrix

Created on Thu Apr  5 06:10:40 2020
@author: Govinda KC

"""
import numpy as np, random

class Graph(object):
    def __init__(self, size):
        
        self.adjMatrix = [[0 for col in range(size)] for row in range(size)]
#        self.adjMatrix = [np.zeros(size, dtype=int) for i in range(size)]
        self.size = size

    def addEdges(self, v1, v2):
        if v1 == v2:
            print(f"Edge between same vertex is being added {v1, v2}")
        self.adjMatrix[v1][v2] = 1
        self.adjMatrix[v2][v1] = 1

    def removeEdge(self, v1, v2):
        if self.adjMatrix[v1][v2] == 0:
            print(f"No edge is found between {v1} and {v2}")
            return
        self.adjMatrix[v1][v2] = 0
        self.adjMatrix[v2][v1] = 0
        print(f"{v1} to {v2} is removed")

    def checkEdge(self, v1, v2):
        return True if self.adjMatrix[v1][v2] > 0 else False

    def matrixSize(self):
        return len(self.adjMatrix)

    def edgeList(self, size):
        EL = [[random.randint(0,size-1) for i in range(2)] for i in range(size-1)]
        return EL
        
def main():
        gp = Graph(5)
        EL = gp.edgeList(5)
        for i in EL:
            gp.addEdges(i[0], i[1])
        print(gp.adjMatrix)
        print(gp.checkEdge(1,2))
        print(gp.matrixSize())
        gp.removeEdge(1,2)
        print(gp.adjMatrix)
            
if __name__ == '__main__':
   main()
