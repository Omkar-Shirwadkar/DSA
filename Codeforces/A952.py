t = int(input())
for _ in range(t):
    a = [s for s in input().split()]
    print(a[1][0] + a[0][1:] + " " + a[0][0] + a[1][1:])