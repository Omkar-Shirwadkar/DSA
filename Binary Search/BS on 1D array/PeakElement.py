def PeakElement(nums, n):

    if n == 1:
        return 0
    
    if nums[0] > nums[1]:
        return 0
    
    if nums[n - 1] > nums[n - 2]:
        return n - 1
    
    l, r = 1, n - 2
    while (l <= r):
        m = (l + r) // 2

        if nums[m] > nums[m - 1] and nums[m] > nums[m + 1]:
            return m
        
        # Peak element is on the left side
        if nums[m] > nums[m + 1]:
            r = m - 1
        
        # Peak element is on the right side
        else:
            l = m + 1

if __name__ == "__main__":
    arr = [1,2,1,3,5,6,4]
    n = len(arr)
    print("Index of Peak element: ", PeakElement(arr, n))