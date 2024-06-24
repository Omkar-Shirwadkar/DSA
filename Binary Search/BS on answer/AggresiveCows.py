def checkm(arr, m, k):
    curr = arr[0]
    groups = 1
    for i in range(1, len(arr)):
        if arr[i] - curr >= m:
            curr = arr[i]
            groups += 1
            if groups == k:
                return 1
    return 0

def aggressiveCows(stalls, k):
    stalls.sort()
    l, r = 0, stalls[-1] - stalls[0]
    while l <= r:
        m = (l + r) // 2
        possible = checkm(stalls, m, k)
        if possible:
            l = m + 1
        else:
            r = m - 1
    return r

if __name__ == "__main__":
    stalls = [0, 3, 4, 7, 10, 9]
    k = 4
    ans = aggressiveCows(stalls, k)
    print("The maximum possible minimum distance is:", ans)