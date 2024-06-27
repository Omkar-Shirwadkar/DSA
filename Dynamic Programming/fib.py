def recur(n):
    if n <= 1:
        return n
    return recur(n - 1) + recur(n - 2)

def memoi(n, arr):
    if n <= 1:
        return n
    if arr[n] != -1:
        return arr[n]
    arr[n] = memoi(n - 1, arr) + memoi(n - 2, arr)
    return arr[n]

def tabul(n):
    dp = [0] * (n + 1)
    dp[0] = 0
    if n >= 1:
        dp[1] = 1
    for i in range(2, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]
    return dp[n]

def space(n):
    if not n:
        return n
    prev = 1
    prevprev = 0
    for _ in range(2, n + 1):
        curr = prev + prevprev
        prevprev = prev
        prev = curr
    return prev

if __name__ == "__main__":
    n = int(input("Enter a number: "))
    print(n, "th Fibonacci numberby recursion: ", recur(n))
    
    dp = [-1] * (n + 1)
    print(n, "th Fibonacci number by memoization: ", memoi(n, dp))

    print(n,"th Fibonacci number by Tabulation: ", tabul(n))

    print(n, "th Fibonacci number by space optimization: ",space(n))