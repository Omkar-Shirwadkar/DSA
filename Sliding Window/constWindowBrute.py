def maxsum(arr, n, k):
    ans = 0
    for i in range(k):
        ans += arr[i]
    l, r = 0, k - 1
    res = ans
    while r < n - 1:
        ans -= arr[l]
        l += 1
        r += 1
        ans += arr[r]
        res = max(res,ans)
    return res

t = int(input())
for _ in range(t):
    n, k = [int(x) for x in input().split()]
    arr = [int(s) for s in input().split()]
    print(maxsum(arr, n, k))