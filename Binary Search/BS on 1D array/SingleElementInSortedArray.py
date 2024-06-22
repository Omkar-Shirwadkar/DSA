def SingleElementInArray(arr, n):
    if n == 1:
        return arr[0]
        
    if arr[0] != arr[1]:
        return arr[0]
    
    if arr[-1] != arr[-2]:
        return arr[-1]
    
    l, r = 1, n - 2
    
    while l <= r:
        m = (l + r) // 2
    
        if arr[m] != arr[m - 1] and arr[m] != arr[m + 1]:
            return arr[m]
        
        # Odd index
        if m & 1:
            #The element is in the right cuz repeated values are at even, odd ==> 0,1
            if arr[m] == arr[m - 1]:
                l = m + 1
            #The element is in the left cuz repeated values are at odd, even ==>  5, 6
            else:
                r = m - 1
        
        # Even index
        else:
            #The element is in the right cuz repeated values are at even, odd ==> 0,1
            if arr[m] == arr[m + 1]:
                l = m + 1
            #The element is in the left cuz repeated values are at odd, even ==>  5, 6
            else:
                r = m - 1

if __name__ == "__main__":
    arr = [1,1,2,2,3,3,4,5,5,6,6,7,7,8,8,9,9,11,11,12,12,13,13,14,14,15,15]
    n = len(arr)
    print("Single Element present in the array: ", SingleElementInArray(arr, n))