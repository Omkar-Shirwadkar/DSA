def numIslands(grid):
    def dfs(grid, i, j):
        if i < 0 or j < 0 or i >= len(grid) or j >= len(grid[0]) or grid[i][j] != 1:
            return
        grid[i][j] = "$"
        dfs(grid, i + 1, j)
        dfs(grid, i, j + 1)
        dfs(grid, i - 1, j)
        dfs(grid, i, j - 1)
        dfs(grid, i - 1, j - 1)
        dfs(grid, i + 1, j + 1)
        dfs(grid, i - 1, j + 1)
        dfs(grid, i + 1, j - 1)
    count = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == 1:
                dfs(grid, i, j)
                count += 1
    return count

def bfs(grid, i, j):
    queue = [[i, j]]
    n = len(grid)
    m = len(grid[0])
    while queue:
        first = queue[0][0]
        second = queue[0][1]
        queue.pop(0)
        grid[first][second] = "$"
        if first + 1 < n and grid[first + 1][second] == 1:
            queue.append([first + 1, second])
        if first - 1 > -1 and grid[first - 1][second] == 1:
            queue.append([first - 1, second])
        if second + 1 < m and grid[first][second + 1] == 1:
            queue.append([first, second + 1])
        if second - 1 > -1 and grid[first][second - 1] == 1:
            queue.append([first, second - 1])

if __name__ == "__main__":
    matrix = [[1,1,0,1,1],[1,1,0,1,1],[0,0,1,0,0],[1,1,0,1,0],[1,1,0,0,1]]
    print("Number of Islands: ", numIslands(matrix))    