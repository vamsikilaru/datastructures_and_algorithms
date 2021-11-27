from graph import Graph

def find_mother_vertex(g:Graph):
    visited = [False]*g.vertices
    last_v = 0
    for i in range(g.vertices):
        if not visited[i]:
            dfs(g,i,visited)
            last_v = i

    visited = [False]*g.vertices
    dfs(g,last_v,visited)
    if any(not i for i in visited):
        return -1
    else:
        return last_v

def dfs(g:Graph,node,visited):
    visited[node]=True
    head_node = g.array[node].head_node
    while head_node:
        if not visited[head_node.value]:
            dfs(g,head_node.value,visited)
        head_node = head_node.next

if __name__ =="__main__":
    g = Graph(4)
    g.add_edge(0,1)
    g.add_edge(1,2)
    g.add_edge(3,0)
    g.add_edge(3,1)
    print(find_mother_vertex(g))
