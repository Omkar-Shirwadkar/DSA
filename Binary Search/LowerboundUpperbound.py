# smallest index where arr[ind] >= target
def LowerBound(arr, n, target):
    l, r = 0, n - 1
    ans = n
    while l <= r:
        m = (l + r) // 2
        if arr[m] >= target:
            ans = m
            r = m - 1
        else:
            l = m + 1
    return ans

# smallest index where arr[ind] > target
def UpperBound(arr, n, target):
    l, r = 0, n - 1
    ans = n
    while l <= r:
        m = (l + r) // 2
        if arr[m] > target:
            ans = m
            r = m - 1
        else:
            l = m + 1
    return ans

if __name__ == "__main__":
    nums = [1,2,3,3,5,8,8,10,10,11]
    n = len(nums)
    while True:
        target =int(input("Enter a target value: "))
        if target == -1:
            break
        print("Lowerbound index: ", LowerBound(nums, n, target))
        print("Upperbound index: ", UpperBound(nums, n, target))