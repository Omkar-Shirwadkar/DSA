t = int(input())
for _ in range(t):
    n = int(input())
    a = [int(x) for x in input().split()]
    if n & 1:
        maxa = max(a)
        found = False
        for i in range(0,n,2):
            if a[i] == maxa:
                found = True
                break
        if found:
            ans = maxa + (n + 1) // 2
        else:
            ans = maxa + (n - 1) // 2
        print(ans)
    else:
        maxa = max(a)
        ans = maxa + n//2
        print(ans)