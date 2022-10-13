from sys import path
import os.path
path.insert(1,os.path.abspath('./stacksAndQueues'))
from queue import Queue
from graph import Graph

def min_distance(g:Graph, source, target):
    visited = [False]* g.vertices
    distance = [0] * g.vertices
    result = 0
    myQueue = Queue()
    myQueue.enqueue(source)
    visited[source] = True

    while not myQueue.is_empty():
        node = myQueue.dequeue()
        temp = g.array[node].head_node
        while temp is not None:
            if not visited[temp.value] or temp.value is target:
                myQueue.enqueue(temp.value)
                visited[temp.value] = True
                distance[temp.value] = distance[node]+1
                if temp.value is target:
                    return distance[target]
            temp = temp.next
    return -1

if __name__ == "__main__" :

    g = Graph(7)
    g.add_edge(1, 2)
    g.add_edge(1, 3)
    g.add_edge(2, 4)
    g.add_edge(4, 5)
    g.add_edge(2, 5)
    g.add_edge(5, 6)
    g.add_edge(3, 6)

    print(min_distance(g, 1, 5))