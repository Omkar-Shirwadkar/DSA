t = int(input())
for _ in range(t):
    n = int(input())
    a = [int(s) for s in input().split()]
    ans = 0
    currsum = 0
    currmax = float("-inf")
    for i in range(n):
        if a[i] > currmax:
            currsum += max(0, currmax)
            currmax = a[i]
        else:
            currsum += a[i]
        if currsum == currmax:
            ans += 1
    print(ans)