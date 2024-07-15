t = int(input())
for _ in range(t):
    n, k = [int(i) for i in input().split()]
    if n == 1:
        print(0)
        continue
    ans = 0
    while n > 1:
        n -= (k - 1)
        ans += 1
    print(ans)