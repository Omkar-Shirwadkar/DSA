t = int(input())
for _ in range(t):
    n = int(input())
    arr = []
    y1 = []
    y0 = []
    for i in range(n):
        x, y = [int(s) for s in input().split()]
        if y:
            y1.append(x)
        else:
            y0.append(x)
    ans = 0
    y1.sort()
    y0.sort()
    set1 = set(y1)
    set0 = set(y0)
    i, j = 0, 0
    l1 = len(y1)
    l0 = len(y0)
    while i < l1 and j < l0:
        if y1[i] == y0[j]:
            ans += (n - 2)
            i += 1
            j += 1
        elif y1[i] < y0[j]:
            i += 1
        else:
            j += 1
    for i in range(l0):
        if y0[i] + 2 in set0 and y0[i] + 1 in set1:
            ans += 1
    for i in range(l1):
        if y1[i] + 2 in set1 and y1[i] + 1 in set0:
            ans += 1
    print(ans)