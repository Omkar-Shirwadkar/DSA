t = int(input())
for _ in range(t):
    n = int(input())
    binn = bin(n)[2:]
    temp = 1
    k = binn.count("1")
    ans = [0] * (k)
    i = k
    while i:
        curr = n ^ temp
        if curr < n:
            ans[i - 1] = curr
            i -= 1
        temp = temp << 1
    ans.append(n)
    print(*ans)