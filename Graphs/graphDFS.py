from sys import path
import os.path
path.insert(1,os.path.abspath('./stacksAndQueues'))
from queue import Queue
from graph import Graph
from stack import Stack

def dfs_helper(g:Graph,source,visited):
    result = ''
    s = Stack()
    s.push(source)
    visited[source]=True
    while not s.is_empty():
        vertex = s.pop()
        node = g.array[vertex].get_head()
        result += str(vertex)
        while node:
            if not visited[node.value]:
                s.push(node.value)
                visited[node.value]=True
            node = node.next
    return result,visited



def dfs(g:Graph,source:int):
    result = ''
    visited =[False]* g.vertices
    result,visited = dfs_helper(g,source,visited)
    for i in range(g.vertices):
        if not visited[i]:
            result_new,visited = dfs_helper(g,i,visited)
            result += result_new
    return result

if __name__ == "__main__" :
    g = Graph(7)
    num_of_vertices = g.vertices
    if num_of_vertices == 0:
        print("Graph is empty")
    elif num_of_vertices < 0:
        print("Graph cannot have negative vertices")
    else:
        g.add_edge(1, 2)
        g.add_edge(1, 3)
        g.add_edge(2, 4)
        g.add_edge(2, 5)
        g.add_edge(3, 6)
        print(dfs(g, 1))