#First Occurence is same as lower bound if number is present else -1
def firstOccurence(nums, n, target):
    ans = -1
    l, r = 0, n - 1
    while l <= r:
        m = (l + r) // 2
        if nums[m] == target:
            ans = m
            r = m - 1
        elif nums[m] > target:
            r = m - 1
        else:
            l = m + 1
    return ans

#Lasr Occurence is same as (upper bound - 1)th index if lower bound exists and is within bounds 
def lastOccurence(nums, n, target):
    ans = -1
    l, r = 0, n - 1
    while l <= r:
        m = (l + r) // 2
        if nums[m] == target:
            ans = m
            l = m + 1
        elif nums[m] > target:
            r = m - 1
        else:
            l = m + 1
    return ans

def totalOccurences(nums, n, target):
    first = firstOccurence(nums, n, target)
    last = lastOccurence(nums, n, target)
    if first == -1:
        return 0
    else:
        return last - first + 1

if __name__ == "__main__":
    arr = [1,1,1,1,2,43,43,43,43,43,67,78,98,89,123,124,456,786]
    n = len(arr)
    target = int(input("Enter target: "))
    print("First Occurence: ", firstOccurence(arr, n, target))
    print("Last Occurence: ", lastOccurence(arr, n, target))
    print("Total Number of Occurences: ", totalOccurences(arr, n, target))