def minimumInRotatedSortedArray(arr, n):
    l, r = 0, n - 1
    ans = float("inf")
    while l <= r:
        #Optimization: if array is sorted no need to perform further binary search on it, hence break
        if arr[l] <= arr[r]:
            ans = min(ans, arr[l])
            break


        m = (l + r) // 2

        if arr[l] <= arr[m]:
            ans = min(ans, arr[l])
            l = m + 1
        
        else:
            ans = min(ans, arr[m])
            r = m - 1

    return ans

if __name__ == "__main__":
    arr = [1000,1023,3210,3423,5234,5439,5544,1,2,43,67,78,98,89,123,124,456,786]
    n = len(arr)
    print("Minimum value in the array is: ", minimumInRotatedSortedArray(arr, n))