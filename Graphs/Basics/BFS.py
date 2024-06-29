def bfsOfGraph(V, adj, start):
    vis = [0] * V
    vis[start] = 1
    q = [start]
    ans = []
    while q:
        ele = q[0]
        q.pop(0)
        ans.append(ele)
        for i in adj[ele]:
            if not vis[i]:
                vis[i] = 1
                q.append(i)
    return ans

#Space Complexity: O(3V)
#Time Complexity: O(V + E)

if __name__ == "__main__":
    V = 5 
    E = 4
    adj = [{1,2,3},{},{4},{},{}]
    start = 0
    print("BFS Traversal: ", bfsOfGraph(V, adj, start))