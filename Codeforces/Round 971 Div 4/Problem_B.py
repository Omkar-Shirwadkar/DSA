t = int(input())
for _ in range(t):
    n = int(input())
    arr = []
    for i in range(n):
        sp = input()
        arr.append(sp)
    ans = []
    for i in range(n - 1, -1, -1):
        pos = arr[i].index("#") + 1
        ans.append(pos)
    print(*ans)