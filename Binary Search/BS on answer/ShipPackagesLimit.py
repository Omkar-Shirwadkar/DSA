def checkIfValid(arr, m, d):
    currsum = 0
    days = 1
    for i in arr:
        currsum += i
        if currsum > m:
            currsum = i
            days += 1
            if days > d:
                return 0
    return 1

def leastWeightCapacity(weights, d):
    l, r = min(weights), sum(weights)
    while (l <= r):
        m = (l + r) // 2
        res = checkIfValid(weights, m, d)
        if res:
            r = m - 1
        else:
            l = m + 1
    return l

if __name__ == "__main__":
    arr = [5, 4, 5, 2, 3, 4, 5, 6]
    days = 5
    print("Least Weight Capacity needed: ", leastWeightCapacity(arr, days))