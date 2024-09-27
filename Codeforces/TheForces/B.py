t = int(input())
for _ in range(t):
    n = int(input())
    bina = bin(n)[2:]
    first = 2 ** (len(bina) - 1)
    second = first - 1
    print(first * second)