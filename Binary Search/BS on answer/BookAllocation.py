def checkmid(arr, n, mid, students):
    curr = arr[0]
    studs = 1
    for i in range(1, n):
        if arr[i] + curr > mid:
            studs += 1
            curr = arr[i]
        else:
            curr += arr[i]
    if studs > students:
        return 0
    return 1

def findPages(arr, n, thugs):
    if thugs > n:
        return -1
    l, r = max(arr), sum(arr)
    while l <= r:
        m = (l + r) // 2
        if checkmid(arr, n, m, thugs):
            r = m - 1
        else:
            l = m + 1
    return l

if __name__ == "__main__":
    arr = [25, 46, 28, 49, 24]
    n = len(arr)
    students = 4
    print("Mninimum Number of pages: ", findPages(arr, n, students))   