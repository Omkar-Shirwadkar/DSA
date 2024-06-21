def iterativeBS(nums, n, target):
    l, r = 0, n - 1
    while l <= r:
        m = (l + r) // 2
        if nums[m] == target:
            return m
        elif nums[m] > target:
            r = m - 1
        else:
            l = m + 1
    return -1

def recursiveBS(arr, l, r, target):
    if l > r:
        return -1
    m = (l + r) // 2
    if arr[m] == target:
        return m
    elif arr[m] > target:
        return recursiveBS(arr, l, m - 1, target)
    else:
        return recursiveBS(arr, m + 1, r, target)

if __name__ == "__main__":
    arr = [12,23,34,35,56,78,89,154,179,257]
    n = len(arr)
    target = int(input())
    print(iterativeBS(arr, n, target))
    print(recursiveBS(arr, 0, n -1, target))