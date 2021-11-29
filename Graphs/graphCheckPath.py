# perform BFS (or DFS) and check if the path exists

from sys import path
import os.path
path.insert(1,os.path.abspath('./stacksAndQueues'))

from graph import Graph
from queue import Queue

def check_path(g:Graph,source,dest):
    
    vistied = [False]*g.vertices
    q = Queue()
    q.enqueue(source)
    vistied[source]=True

    while not q.is_empty():
        node = q.dequeue()
        if node == dest:
            return True
        
        head = g.array[node].head_node
        while head:
            if not vistied[head.value]:
                vistied[head.value]= True
                q.enqueue(head.value)
            head = head.next
    return False

if __name__ == "__main__" :

    g1 = Graph(9)
    g1.add_edge(0, 2)
    g1.add_edge(0, 5)
    g1.add_edge(2, 3)
    g1.add_edge(2, 4)
    g1.add_edge(5, 3)
    g1.add_edge(5, 6)
    g1.add_edge(3, 6)
    g1.add_edge(6, 7)
    g1.add_edge(6, 8)
    g1.add_edge(6, 4)
    g1.add_edge(7, 8)
    g2 = Graph(4)
    g2.add_edge(0, 1)
    g2.add_edge(1, 2)
    g2.add_edge(1, 3)
    g2.add_edge(2, 3)

    print(check_path(g1, 0, 7))
    print(check_path(g2, 3, 0))
