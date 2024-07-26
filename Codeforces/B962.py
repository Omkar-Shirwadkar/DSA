t = int(input())
for _ in range(t):
    n, k = [int(x) for x in input().split()]
    arr = []
    for i in range(n):
        s = input()
        arr.append(s)
    res = []
    for i in range(0, n, k):
        bro = []
        for j in range(0, n, k):
            bro.append(arr[i][j])
        res.append(bro)
    for i in range(len(res)):
        print("".join(res[i]))