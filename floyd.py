 
def floydWarshall(graph):           
    dist=graph   
    for k in range(V):          
        for i in range(V):              
            for j in range(V):                   
                dist[i][j] = min(dist[i][j] ,dist[i][k]+ dist[k][j] ) 
    printSolution(dist)
    
def printSolution(dist): 
    print ("matrix of the shortest distances")
    for i in range(V):
        for j in range(V):
            print(dist[i][j],end='\t')
        print()
  
  
  
INF  = 99999  
V=5
graph = [    [0,2,INF,1,8], 
             [6,0,3,2,INF], 
             [INF, INF, 0,4,INF], 
             [INF, INF, 2, 0 ,3],
             [3,INF,INF,INF,0],
        ] 

floydWarshall(graph); 

