t = int(input())
for _ in range(t):
    x, y = [int(s) for s in input().split()]
    x = bin(x)[2:]
    y = bin(y)[2:]
    x = "0" * (max(0, len(y) - len(x))) + x
    y = "0" * (max(0, len(x) - len(y))) + y
    ans = 1
    i = 0
    while(i < len(x)):
        if x[len(x) - i - 1] ==y[len(x) - i - 1]:
            ans += 2 ** i
            i += 1
        else:
            break
    print(ans)