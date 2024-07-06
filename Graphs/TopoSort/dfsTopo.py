def topoSort(V, adj):
    vis = [0] * V
    ans = []
    def dfs(idx):
        vis[idx] = 1
        for i in adj[idx]:
            if not vis[i]:
                dfs(i)
        ans.append(idx)
    for i in range(V):
        if not vis[i]:
            dfs(i)
    return ans[:: -1]

if __name__ == "__main__":
    V = 6
    adj = [
        [],
        [],
        [3],
        [1],
        [0,1],
        [0,2]
    ]
    print(topoSort(V, adj))