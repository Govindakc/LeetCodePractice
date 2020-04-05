class Graph(object):
    def __init__(self, size):
        
#         self.adjMatrix = [[0 for col in range(size)] for row in range(size)]
        self.adjMatrix = [np.zeros(size, dtype=int) for i in range(size)]
        self.size = size

    def addEdge(self, v1, v2):
        if v1 == v2:
            print("Same vertex %d and %d" % (v1, v2))
        self.adjMatrix[v1][v2] = 1
        self.adjMatrix[v2][v1] = 1

    def removeEdge(self, v1, v2):
        if self.adjMatrix[v1][v2] == 0:
            print("No edge between %d and %d" % (v1, v2))
            return
        self.adjMatrix[v1][v2] = 0
        self.adjMatrix[v2][v1] = 0
        print(f"{v1} to {v2} is removed")

    def containsEdge(self, v1, v2):
        return True if self.adjMatrix[v1][v2] > 0 else False

    def matrixSize(self):
        return len(self.adjMatrix)

    def edge_list(self, size):
        EL = [[random.randint(0,size-1) for i in range(2)] for i in range(size-1)]
        
        return EL
        
def main():
        gp = Graph(5)
        EL = gp.edge_list(5)
        for i in EL:
            gp.addEdge(i[0], i[1])
        print(gp.adjMatrix)
        print(gp.containsEdge(1,2))
        print(gp.matrixSize())
        gp.removeEdge(1,2)
        print(gp.adjMatrix)
            
if __name__ == '__main__':
   main()
