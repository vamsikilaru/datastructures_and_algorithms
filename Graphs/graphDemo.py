
from graph import Graph
import os.path
print(os.path.abspath("./.."))

if __name__ == "__main__":
    g = Graph(4)
    g.add_edge(0,1)
    g.add_edge(0,2)
    g.add_edge(1,3)
    g.add_edge(2,3)
    g.print_graph()
