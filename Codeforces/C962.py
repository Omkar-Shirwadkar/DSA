t = int(input())
for _ in range(t):
    n, q = [int(s) for s in input().split()]
    a = input()
    b = input()
    arr1 = [0] * 26
    arr2 = [0] * 26
    for w in range(q):
        l, r = [int(s) for s in input().split()]
        for i in range(l - 1, r):
            arr1[ord(a[i]) - ord("a")] += 1
            arr2[ord(b[i]) - ord("a")] += 1
        ans = 0
        for i in range(26):
            if arr1[i] != arr2[i]:
                ans += abs(arr1[i] - arr2[i])
            arr1[i] = 0
            arr2[i] = 0
        print(ans // 2)