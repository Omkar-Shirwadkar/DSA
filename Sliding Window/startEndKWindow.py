def pickKItems(arr, n, k):
    lsum = rsum = maxsum = 0
    for i in range(k):
        lsum += arr[i]
    maxsum = lsum
    print(lsum, rsum)
    for i in range(k):
        lsum -= arr[k - i - 1]
        rsum += arr[n - i - 1]
        print(lsum, rsum)
        maxsum = max(lsum + rsum, maxsum)
    return maxsum

t = int(input())
for _ in range(t):
    n, k = [int(x) for x in input().split()]
    arr = [int(s) for s in input().split()]
    print(pickKItems(arr, n, k))