def findCircleNum(isConnected):
    def dfs(x):
        visited[x] = True
        for i in range(n):
            if isConnected[x][i] == 1 and not visited[i]:
                dfs(i)
    n = len(isConnected)
    c = 0
    visited = [False] * n
    for i in range(n):
        if not visited[i]:
            c += 1
            dfs(i)
    return c

if __name__ == "__main__":
    matrix = [[1,1,0,1,1],[1,1,0,1,1],[0,0,1,0,0],[1,1,0,1,0],[1,1,0,0,1]]
    print("Number of Provinces: ", findCircleNum(matrix))