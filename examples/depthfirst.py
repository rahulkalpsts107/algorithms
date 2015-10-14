#depth first traversal of a graph
#make sure to hold an adjacency matrix as well as a memoization trick to avoid nasty recursion
#time complexity for recursion is at max is Number of vertices and Edges considering each Vertex has unique edges

from datetime import datetime

class Graph:
    def __init__(self,num):
        self.num = num
        self.adjList = {}

    def addToGraph(self,V,E):
        if(V in self.adjList):
            self.adjList[V].update({E})
        else:
            self.adjList[V] ={E}

def runDFSStack(g,key,visited):
    stack = []
    stack.append(key)
    for key in stack:
        stack.pop()
        if(visited[key]== False):
            visited[key]={True}
            print('Node '+str(key))
            for vex in g.adjList[key]:
                stack.append(vex)



def runDFS(g,key,visited):
    visited[key]={True}
    print('Node '+str(key))
    #print(visited)
    for key in g.adjList:
        if(visited[key] == False):
            runDFS(g,key,visited)

def run():
    graphNodes = 11
    g= Graph(graphNodes)
    g.addToGraph(0,1)
    g.addToGraph(0,2)
    g.addToGraph(1,2)
    g.addToGraph(2,0)
    g.addToGraph(2,3)
    g.addToGraph(3,3)
    g.addToGraph(4,3)
    g.addToGraph(5,1)
    g.addToGraph(1,5)
    g.addToGraph(4,5)
    g.addToGraph(5,1)
    g.addToGraph(6,5)
    g.addToGraph(7,6)
    g.addToGraph(8,7)
    g.addToGraph(9,8)
    g.addToGraph(10,9)
    visited = [False]*graphNodes #damn this is too cool
    now = datetime.now()
    for key in range(0,graphNodes):
        if(visited[key] == False):
            #runDFS(g,key,visited)
            runDFSStack(g,key,visited)
    later = datetime.now()
    print (g.adjList)
    diff = (later - now)
    print('Time '+str(diff))

if __name__ == '__main__':
    run()
