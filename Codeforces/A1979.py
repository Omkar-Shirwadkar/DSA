t = int(input())
for _ in range(t):
    n = int(input())
    a = [int(s) for s in input().split()]
    maxa = [0] * (n - 1)
    for i in range(1, n):
        maxa[i - 1] = max(a[i], a[i - 1])
    maxa.sort()
    print(maxa[0] - 1)