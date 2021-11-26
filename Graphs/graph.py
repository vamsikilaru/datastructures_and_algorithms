from sys import path
import os.path
path.insert(1,os.path.abspath("./LinkedLists"))
from linkedList import LinkedList
 
class Graph:
    def __init__(self, vertices) -> None:
        self.vertices = vertices
        self.array = []
        for _ in range(self.vertices):
            self.array.append(LinkedList())

    def add_edge(self,source,destination):
        if source < self.vertices and destination < self.vertices:
            self.array[source].insert_at_head(destination)  # this is a directed graph
            # for undirected graph add edge in both the directions
            # self.array[destination].insert_at_head(source)

        # If we were to implement an Undirected Graph i.e (1,0) == (0,1)
        # We would create an edge from destination towards source as well
        # i.e self.list[destination].insertAtHead(source)

    def print_graph(self):
        print(">> Adjacency List of Directed graph <<")
        for i in range(self.vertices):
            print("|",i,end=" | => ")
            temp = self.array[i].get_head()
            while temp:
                print("[",temp.value,end=" ] -> ")
                temp = temp.next
            print("None")