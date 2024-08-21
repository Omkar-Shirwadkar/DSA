t = int(input())
for _ in range(t):
    n, s, m = [int(x) for x in input().split()]
    arr = []
    for a in range(n):
        l, r = [int(x) for x in input().split()]
        arr.append([l, r])
    arr.sort()
    curr = 0
    end = m
    ans = False
    for i in range(n):
        if arr[i][0] - curr >= s:
            ans = True
            print("YES")
            break
        else:
            curr = arr[i][1]
    if not ans:
        if end - curr >= s:
            print("YES")
        else:
            print("NO")