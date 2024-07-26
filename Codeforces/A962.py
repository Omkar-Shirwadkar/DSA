t = int(input())
for _ in range(t):
    n = int(input())
    if n % 4:
        print(n // 4 + 1)
    else:
        print(n // 4)