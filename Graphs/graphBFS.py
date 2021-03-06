from sys import path
import os.path
path.insert(1,os.path.abspath('./stacksAndQueues'))
from queue import Queue
from graph import Graph

def bfs_helper(g: Graph,source:int,visited:list):
    result = ''
    q = Queue()
    q.enqueue(source)
    visited[source]= True
    while not q.is_empty():
        vertex = q.dequeue()
        result += str(vertex)
        node = g.array[vertex].get_head()
        while node:
            if not visited[node.value]:
                q.enqueue(node.value)
                visited[node.value] = True
            node = node.next
    return result,visited

def bfs(g:Graph,source:int):
    visited = [False]*g.vertices
    result = ''
    result,visited = bfs_helper(g,source,visited)
    for i in range(g.vertices):
        if not visited[i]:
            result_new,visited = bfs_helper(g,i,visited)
            result += result_new
    return result
        


if __name__ == "__main__":
    g = Graph(4)
    g.add_edge(0,1)
    g.add_edge(0,2)
    g.add_edge(1,3)
    g.add_edge(2,3)
    print(bfs(g,0))