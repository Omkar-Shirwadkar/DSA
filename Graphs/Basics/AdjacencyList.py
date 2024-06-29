def printGraph(V, edges):
    adj = [[] for _ in range(V)]
    for u, v in edges:
        adj[u].append(v)
        adj[v].append(u)
    return adj

if __name__ == "__main__":
    V = 5
    E = 7
    edges = [(0,1),(0,4),(4,1),(4,3),(1,3),(1,2),(3,2)]
    print("Adjacency List: ", printGraph(V, edges))