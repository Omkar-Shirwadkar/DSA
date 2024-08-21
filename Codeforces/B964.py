t = int(input())
for i in range(t):
    a1, a2, b1, b2 = [int(x) for x in input().split()]
    ans = 0
    if a1 > b1 and a2 > b2:
        ans += 2
    if a1 > b2 and a2 > b1:
        ans += 2
    print(ans)