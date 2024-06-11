t = int(input())
for _ in range(t):
    n, m = [int(s) for s in input().split()]
    ele = []
    for i in range(n):
        f = input()
        ele.append(f)
    cnthash = 0
    firsthash = [0,0]
    first = False
    for i in range(n):
        for j in range(m):
            if ele[i][j] == "#":
                cnthash += 1
                if not first:
                    firsthash = [i + 1, j + 1]
                    first = not first
    i = 1
    j = 0
    while i != cnthash:
        cnthash -= i * 2
        j += 1
        i += 2
    firsthash[0] += j
    print(*firsthash)