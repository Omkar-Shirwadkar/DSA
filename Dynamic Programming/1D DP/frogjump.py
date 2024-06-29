def recur(idx, heights):
    if idx == 0:
        return 0
    left = recur(idx - 1, heights) + abs(heights[idx] - heights[idx - 1])
    right = 100000000
    if idx > 1:
        right = recur(idx - 2, heights) + abs(heights[idx] - heights[idx - 2])
    return min(left, right)


def memoi(idx, heights, dp):
    if idx == 0:
        return 0
    if dp[idx] != -1:
        return dp[idx]
    left = memoi(idx - 1, heights, dp) + abs(heights[idx] - heights[idx - 1])
    right = 100000000
    if idx > 1:
        right = memoi(idx - 2, heights, dp) + abs(heights[idx] - heights[idx - 2])
    dp[idx] = min(left, right)
    return dp[idx]

def tabul(n, heights):
    dp = [0] * n
    if n == 1:
        return 0
    dp[0] = 0
    dp[1] = abs(heights[0] - heights[1])
    for i in range(2, n):
        dp[i] = min(dp[i - 1] + abs(heights[i - 1] - heights[i]), dp[i - 2] + abs(heights[i - 2] - heights[i]))
    return dp[-1]

def space(n, heights):
    if n == 1:
        return 0
    seclast = 0
    last = abs(heights[0] - heights[1])
    for i in range(2, n):
        curr = min(last + abs(heights[i - 1] - heights[i]), seclast + abs(heights[i - 2] - heights[i]))
        seclast = last
        last = curr
    return last

def ksteps(n, height, k):
    dp = [0] * (n)
    dp[0] = 0
    for i in range(1, n):
        mini = 10000000000
        for j in range(1, k + 1):
            if i - j > -1:
                mini = min(mini, dp[i - j] + abs(height[i] - height[i - j]))
        dp[i] = mini
    return dp[-1]

if __name__ == "__main__":
    arr = [30, 10, 60, 10, 60, 50]
    n = len(arr) - 1
    print("Minimum cost to reach the top by Recursion: ", recur(n, arr))

    dp = [-1] * (n + 1)
    print("Minimum cost to reach the top by Memoization: ", memoi(n, arr, dp))

    print("Minimum cost to reach the top by Tabulation: ", tabul(n + 1, arr))

    print("Minimum cost to reach the top by Space Optimization: ", space(n + 1, arr))
    k = 3
    print("Minimum cost to reach the top with maximum jump of k steps by Tabulation: ", ksteps(n, arr, k))