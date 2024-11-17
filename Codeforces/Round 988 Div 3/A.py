t = int(input())
for _ in range(t):
    n = int(input())
    a = [int(x) for x in input().split()]
    nary = {}
    for i in a:
        if i in nary:
            nary[i] += 1
        else:
            nary[i] = 1
    ans = 0
    for i in nary.values():
        ans += i // 2
    print(ans)