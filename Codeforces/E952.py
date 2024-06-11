t = int(input())
for _ in range(t):
    x, y, z, k = [int(s) for s in input().split()]
    ans = 0
    for a in range(1, x + 1):
        if not k % a:
            rem1 = k // a
            for b in range(1, y + 1):
                if not rem1 % b:
                    c = rem1 // b
                    if c <= z and a * b * c == k:
                        ans = max(ans, (x - a + 1)*(y - b + 1)*(z - c + 1))
    print(ans)