from collections import deque
def topoSort(V, adj):
    indegree = [0] * V
    for i in range(V):
        for j in adj[i]:
            indegree[j] += 1
    queue = deque()
    ans = []
    for i in range(V):
        if not indegree[i]:
            queue.append(i)
    while queue:
        ele = queue.popleft()
        ans.append(ele)
        for i in adj[ele]:
            indegree[i] -= 1
            if not indegree[i]:
                queue.append(i)
    return ans

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