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
            self.array[source].insert_at_head(destination)

    def print_graph(self):
        print(">> Adjacency List of Directed graph <<")
        for i in range(self.vertices):
            print("|",i,end=" | => ")
            temp = self.array[i].get_head()
            while temp:
                print("[",temp.value,end=" ] -> ")
                temp = temp.next
            print("None")