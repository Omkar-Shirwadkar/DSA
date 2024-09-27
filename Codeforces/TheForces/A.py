t = int(input())
for _ in range(t):
    a,b = [int(s) for s in input().split()]
    i = max(0, a - 4 + 1)
    j = max(0, b - 6 + 1)
    ans = i * j
    print(ans)