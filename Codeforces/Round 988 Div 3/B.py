import math
t = int(input())
for _ in range(t):
    n = int(input())
    a = [int(x) for x in input().split()]
    dimen = n - 2
    ans = False
    res = [1, 1]
    seta = set([i for i in a])
    for i in range(1, int(math.sqrt(dimen)) + 1):
        if dimen % i == 0 and i in seta:
            sec = dimen // i
            if dimen % sec == 0 and sec in seta:
                ans = True
                res = [i, sec]
        if ans:
            break
    print(*res)