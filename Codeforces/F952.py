import math
t = int(input())
for _ in range(t):
    h, n = [int(s) for s in input().split()]
    a = [int(s) for s in input().split()]
    c = [int(s) for s in input().split()]
    nary = {}
    for i in range(n):
        if c[i] in nary:
            nary[c[i]] += a[i]
        else:
            nary[c[i]] = a[i]
    myKeys = list(nary.keys())
    myKeys.sort()
    bj = myKeys[0]
    sorted_dict = {i: nary[i] for i in myKeys}
    if sum(a) >= h:
        print(1)
    else:
        sz = (math.ceil(h / sorted_dict[bj])) * bj
        harr = [0] * sz
        for i, j in sorted_dict.items():
            k = 0
            while k * i < sz:
                harr[k * i] += j
                k += 1
        print(harr, len(harr))