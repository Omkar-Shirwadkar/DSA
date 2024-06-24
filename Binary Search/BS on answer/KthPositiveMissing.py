"""
Note:
    1. Given array is sorted in strictly increasing order

Observation:
    1. at any given index " i " the number of missing values is arr[i] - (i + 1) 
    2. After breaking the loop, high index is at an index which is just smaller than k
        i. high points to missing value less than k thus, kth number is (arr[high] + more)
            more = k - missing
            missing = arr[high] - (high + 1)
            therefore kth number = arr[high] + more
                                 = arr[high] + k - arr[high] + high + 1
                                 = low + k
Explanation:
    1. 
    arr =       [2, 3, 4, 7, 11]
    missing =   [1, 1, 1, 3, 6] ==> missing[i] = arr[i] - (i + 1) ==> (2 - 1) = 1, (3 - 2) = 1, (4 - 3) = 1, (7 - 4) = 3, (11 - 5) = 6
"""

def missingK(arr, n, k):
    l, r = 0, n - 1
    while l <= r:
        m = (l + r) // 2
        missing = arr[m] - (m + 1)
        if missing < k:
            l = m + 1
        else:
            r = m - 1
    return l + k

if __name__ == "__main__":
    arr = [2,3,4,7,11]
    k = 5
    n = len(arr)
    print("The Kth missing number in the array: ", missingK(arr,n,k))