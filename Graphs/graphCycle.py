from graph import Graph


def detect_cycle(g:Graph):
    visited = [False] * g.vertices
    rec_node_stack = [False] * g.vertices
    for node in range(g.vertices):
        if detect_cycle_rec(g,node,visited,rec_node_stack):
            return True
    return False

def detect_cycle_rec(g:Graph,node, visited,rec_node_stack):
    if rec_node_stack[node]:
        return True
    if visited[node]:
        return False
    visited[node]=True
    rec_node_stack[node]=True
    print("1",visited,rec_node_stack)
    head_node = g.array[node].head_node
    while head_node:
        adjacent_node = head_node.value
        if detect_cycle_rec(g,adjacent_node,visited,rec_node_stack):
            return True
        head_node = head_node.next
    rec_node_stack[node]= False
    print("2",visited,rec_node_stack)
    return False

if __name__ == "__main__" :
    g1 = Graph(4)
    g1.add_edge(0, 1)
    g1.add_edge(1, 2)
    g1.add_edge(1, 3)
    g1.add_edge(3, 0)
    
    g2 = Graph(3)
    g2.add_edge(0, 1)
    g2.add_edge(1, 2)

    print(detect_cycle(g1))
    print(detect_cycle(g2))