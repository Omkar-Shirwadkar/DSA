def nonAdjacent(idx, nums, dp):
    if idx == 0:
        return nums[0]
    if idx < 0:
        return 0
    if dp[idx] != -1:
        return dp[idx]
    pick = nums[idx] + nonAdjacent(idx - 2, nums, dp)
    notpick = 0 + nonAdjacent(idx - 1, nums, dp)
    dp[idx] = max(pick, notpick)
    return dp[idx]

def tabul(nums, n):
    dp = [0] * n
    dp[0] = nums[0]
    for i in range(1, n):
        take = nums[i]
        if i > 1:
            take += dp[i - 2]
        nottake = 0 + dp[i - 1]
        dp[i] = max(take, nottake)
    return dp[-1]

def space(nums, n):
    prev = nums[0]
    prevprev = 0
    for i in range(1, n):
        take = nums[i]
        if i > 1:
            take += prevprev
        nottake = 0 + prev
        curr = max(take, nottake)
        prevprev = prev
        prev = curr
    return prev

if __name__ == "__main__":
    arr = [1,2,3,1,3,5,8,1,9]
    n = len(arr)
    dp = [-1] * n
    print("Maximum Sum of non adjacent elements by memoization: ",nonAdjacent(n - 1, arr, dp))
    print("Maximum sum of non adjacent elements by tabulation: ", tabul(arr, n))
    print("Maximum sum of non adjacent elements by Space Optimization: ", space(arr, n))