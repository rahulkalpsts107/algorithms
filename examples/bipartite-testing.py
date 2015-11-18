'''
Bipartite with BFS application
Professor Hopper is researching the sexual behavior of a rare species of bugs. He assumes that they feature two different genders and that they only interact with bugs of the opposite gender.
In his experiment, individual bugs and their interactions were easy to identify, because numbers were printed on their backs.

Given a list of bug interactions, decide whether the experiment supports his assumption of two genders with no homosexual bugs or
if it contains some bug interactions that falsify it.

Input

The first line of the input contains the number of scenarios. Each scenario starts with
one line giving the number of bugs (at least one, and up to 2000) and the number of interactions (up to 1000000)
separated by a single space. In the following lines, each interaction is given in the form of two distinct bug numbers
separated by a single space. Bugs are numbered consecutively starting from one.

Output

The output for every scenario is a line containing
“Scenario #i:”, where i is the number of the scenario starting at 1, followed by one line saying either “
# No suspicious bugs found!” if the experiment is consistent with his assumption about the bugs’ sexual behavior, or
# “Suspicious bugs found!” if Professor Hopper’s assumption is definitely wrong.
'''

#Not working !
import sys
red = 1
black = 0
nil = 2
class Node:
    def __init__(self,color,data,parent):
        self.color = color
        self.data = data
        self.pi = parent

def bfs(adj,nodes):
    print(adj)
    q=[]
    s = nodes.get(1)
    node = Node(red,s,None)
    frontier={s}
    level =0
    while(frontier):
        next = []
        for u in frontier:
            if v not in adj:
                v = nodes[u.data]
                if v.color == nil:
                    v.pi = u
                    next.append(v)
                    if u.color == red:
                        v.color = black
                    else:
                        v.color = red
                elif v.color == u.color:
                    return 1
                continue
            for v in adj[u.data]:
                if v.color == nil:
                    v.pi = u
                    next.append(v)
                    if u.color == red:
                        v.color = black
                    else:
                        v.color = red
                elif v.color == u.color:
                    return 1
        frontier = next
    return 0


def run():
    num_of_inputs =0
    sentinel = '' # ends when this string is seen
    num_of_inputs = input('Enter num of inputs')
    num_of_inputs=int(num_of_inputs)
    while(num_of_inputs):
        line = input()
        adj={}
        #print(line) # do things here
        num_of_bugs,num_of_interactions = line.split(' ',2)
        print('num of bugs= '+num_of_bugs+'num_of_interactio= '+num_of_interactions)
        num_of_bugs=int(num_of_bugs)
        num_of_interactions=int(num_of_interactions)
        nodes={}
        for i in range(1,num_of_interactions+1):
            interaction = input()
            u,v = interaction.split(' ',2)
            u=int(u)
            v=int(v)
            print(adj)
            n = Node(nil,v,None)
            if i not in nodes:
                nodes[i]={n}
            else:
                nodes[i].append({n})
            if u in adj:
                adj[u].update({n})
            else:
                adj[u] ={n}
        ret = bfs(adj,nodes)
        if ret == 1:
            print('Not bipartite')
        else:
            print('Bipartite')
        num_of_inputs-=1

if __name__=="__main__":
    run()