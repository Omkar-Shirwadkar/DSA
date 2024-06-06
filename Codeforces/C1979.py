t = int(input())
for _ in range(t):
    n = int(input())
    a = [int(s) for s in input().split()]
    maxa = max(a)
    for i in a:
        maxa *= i
    print(maxa)