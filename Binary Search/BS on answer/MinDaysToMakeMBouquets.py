def minDays(A, m, k):
    if m * k > len(A):
        return -1
    l, r = min(A), max(A)
    while l <= r:
        mid = (l + r) // 2
        curr = bouq = 0
        for i in A:
            if i > mid:
                curr = 0
            else:
                curr += 1
                if curr == k:
                    curr = 0
                    bouq += 1
                    if bouq == m:
                        break
        if bouq == m:
            r = mid - 1
        else:
            l = mid + 1
    return l

if __name__ == "__main__":
    arr = [ 1, 2, 1, 2, 7, 2, 2, 3, 1 ]
    k = 3
    m = 2
    print("Minimum number of days required to make m bouquets of k flowers: ", minDays(arr, m, k))