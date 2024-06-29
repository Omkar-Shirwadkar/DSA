def DFS(node, adj, vis, ans):
    vis[node] = 1
    ans.append(node)
    for i in adj[node]:
        if not vis[i]:
            DFS(i, adj,vis,ans)

#Space Complexity: O(3V)
#Time Complexity: O(V + E)

if __name__ == "__main__":
    V = 5 
    E = 4
    adj = [{1,2,3},{},{4},{},{}]
    start = 0
    vis = [0] * (V + 1)
    ans = []
    DFS(start, adj, vis, ans)
    print("DFS Traversal: ", ans)