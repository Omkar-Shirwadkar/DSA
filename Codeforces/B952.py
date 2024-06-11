t = int(input())
for _ in range(t):
    n = int(input())
    ans = 0
    res = 2
    for i in range(2, n + 1):
        ele = 1
        curr = 0
        while ele * i <= n:
            curr += ele * i
            ele += 1
        if curr > ans:
            ans = curr
            res = i
    print(res)