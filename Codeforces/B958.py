t = int(input())
for _ in range(t):
    n = int(input())
    s = input()
    g1 = 0
    g0 = 0
    max1 = 0
    if s[0] == "0":
        g0 += 1
        curr = "0"
    else:
        g1 += 1
        curr = "1"
    ones = 0
    for i in range(n):
        if s[i] != curr:
            if s[i] == "0":
                g0 += 1
            else:
                g1 += 1
            curr = s[i]
        if s[i] == "1":
            ones += 1
            max1 = max(max1, ones)
        else:
            ones = 0
    l1 = 0
    i = 0
    while i < n and s[i] == "1":
        l1 += 1
        i += 1
    s1 = 0
    i = n - 1
    while i > -1 and s[i] == "1":
        s1 += 1
        i -= 1
    if g1 > g0 or max1 >= 5 or (g1 == 1 and g0 == 1 and max1 > 2) or l1 > 2 or s1 > 2:
        print("YES")
    else:
        print("NO")