from graph import Graph

def is_tree(g:Graph):
    visited = [False]*g.vertices
    if check_cycle(g,0,visited,-1):
        return False
    if any(not i  for i in visited):
        return False
    return True

def check_cycle(g:Graph,node,visited,parent):
    visited[node]=True
    adjacent = g.array[node].head_node
    while adjacent:
        if not visited[adjacent.value]:
            if check_cycle(g,adjacent.value,visited,node):
                return True
        elif adjacent.value is not parent:
            return True
        adjacent = adjacent.next
    return False

if __name__ == "__main__" :

    g = Graph(5)
    g.add_edge(0, 1)
    g.add_edge(0, 2)
    g.add_edge(0, 3)
    g.add_edge(3, 4)

    print(is_tree(g))