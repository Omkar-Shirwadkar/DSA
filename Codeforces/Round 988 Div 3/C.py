import math
t = int(input())
for _ in range(t):
    n = int(input())
    if n < 5:
        print(-1)
    else:
        mid = [2, 4, 5, 1, 3]
        first = []
        last = []
        if n & 1:
            for i in range(6, n, 2):
                first.append(i)
            for i in range(7, n + 1, 2):
                last.append(i)
        else:
            for i in range(6, n + 1, 2):
                first.append(i)
            for i in range(7, n, 2):
                last.append(i)
        ans = first + mid + last
        print(*ans)

