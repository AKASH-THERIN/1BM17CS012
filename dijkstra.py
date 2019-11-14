
import sys 
 
class Graph(): 
     
    def __init__(self, vertices): 
        self.V = vertices 
        self.graph = [[0 for column in range(vertices)]  
                    for row in range(vertices)]
        self.mat = [[0 for column in range(vertices)]  
                    for row in range(vertices)]   
    def printSolution(self, dist): 
        print ("Vertex \tDistance from Source")
        for node in range(self.V): 
            print (node, "\t", dist[node])
        print(self.mat)
    
    def minDistance(self, dist, sptSet):  
        min = sys.maxsize   
        for v in range(self.V): 
            if dist[v] < min and sptSet[v] == False: 
                min = dist[v] 
                min_index = v   
        return min_index
    
    def dijkstra(self, src):   
        dist = [sys.maxsize] * self.V 
        dist[src] = 0
        sptSet = [False] * self.V   
        for cout in range(self.V):           
            u = self.minDistance(dist, sptSet)              
            sptSet[u] = True
            
            for v in range(self.V): 
                if self.graph[u][v] > 0 and sptSet[v] == False and \
                dist[v] > dist[u] + self.graph[u][v]: 
                        dist[v] = dist[u] + self.graph[u][v]
                        self.mat[u][v]=dist[v]
        self.printSolution(dist) 
  

g = Graph(7) 
g.graph = [[0, 3, 0, 5, 0, 0, 0], 
           [3, 0, 2, 1, 0, 0, 0], 
           [0, 2, 0, 4, 4, 0, 1], 
           [5, 1, 4, 0, 0, 3, 0], 
           [0, 0, 4, 0, 0, 2, 5], 
           [0, 0, 0, 3, 2, 0, 6], 
           [0, 0, 1, 0, 5, 6, 0]           
        ]; 
  
g.dijkstra(0); 
