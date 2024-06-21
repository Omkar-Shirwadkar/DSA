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

#Search Insertion Problem ==> Given a sorted array insert a new element target and return its position => should be leftmost as possible
def searchInsertionProblem(arr, n, target):
    return LowerBound(arr, n, target)

# Floor of an array is the largest number in the array which is smaller than or equal to target
def Floor(arr, n, x):
    l, r = 0, n - 1
    ans = -1
    while l <= r:
        m = (l + r) // 2
        if arr[m] <= x:
            ans = arr[m]
            l = m + 1
        else:
            r = m - 1
    return ans

#Ceil of an array is the smallest number in the array which is greater than or equal to target
def Ceil(arr, n, x):
    l, r = 0, n - 1
    ans = -1
    while l <= r:
        m = (l + r) // 2
        if arr[m] >= x:
            ans = arr[m]
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
        print("Floor value: ", Floor(nums, n, target))
        print("Ceil value: ", Ceil(nums, n, target))