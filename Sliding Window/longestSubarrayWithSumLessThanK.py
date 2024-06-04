def brute(arr, n, k):
    maxlen = 0
    for i in range(n):
        suma = 0
        for j in range(i, n):
            suma += arr[j]
            if suma <= k:
                maxlen = max(maxlen, j - i + 1)
            else:
                break
    return maxlen    

def best(arr, n, k):
    l, r = 0, 0
    maxlen = 0
    suma = 0
    while r < n:
        suma += arr[r]
        if suma > k:
            suma -= arr[l]
            l += 1
        if suma <= k:
            maxlen = max(maxlen, r - l + 1)
        r += 1
    return maxlen

t = int(input())
for _ in range(t):
    n, k = [int(x) for x in input().split()]
    arr = [int(s) for s in input().split()]
    print(brute(arr, n, k))
    print(best(arr, n, k))