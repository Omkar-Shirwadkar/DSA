def insertionSort(arr):
    for step in range(1, len(arr)):
        curr = arr[step]
        i = step - 1
        while i >= 0 and curr < arr[i]:
            arr[i + 1] = arr[i]
            i -= 1
        arr[i + 1] = curr
        print(i + 1, "Iteration: ", *arr)

if __name__ == "__main__":
    arr = [2, 6, 8, 12, 45, 21, 1, 3, 49, 7]
    print("Array before sorting: ", *arr)
    insertionSort(arr)
    print("Array after Insertion sort: ", *arr)