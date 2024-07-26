import math
t = int(input())
for _ in range(t):
    n, x = [int(s) for s in input().split()]
    ans = 0
    for a in range(1, x):
        for b in range(1, min(x - a, n // a)):
            c = min(x - a - b, (n - a * b) // (a + b))
            ans += c
    print(ans)