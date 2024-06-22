#Check if the array is left sorted or right sorted
def searchInRotatedSorted(nums, n, target):
    l, r = 0, n - 1
    while l <= r:
        m = (l + r) // 2
        if nums[m] == target:
            return m
        
        # Edge case: when the array contains duplicate value
        # We shrink the search space
        # if nums[l] == nums[m] and nums[r] == nums[m]:
        #     l += 1
        #     r -= 1
        #     continue
        #Left sorted array
        elif nums[l] <= nums[m]:
            if nums[l] <= target and target <= nums[m]:
                r = m - 1
            else:
                l = m + 1
        #Right sorted array
        else:
            if nums[m] <= target and target <= nums[r]:
                l = m + 1
            else:
                r = m - 1
    return -1

if __name__ == "__main__":
    arr = [1000,1023,3210,3423,5234,5439,5544,1,2,43,67,78,98,89,123,124,456,786]
    n = len(arr)
    target = int(input("Enter target: "))
    print("Target found at: ", searchInRotatedSorted(arr, n, target))