def selectionSort(arr, n):
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[min_idx], arr[i] = arr[i], arr[min_idx]
        print(i + 1, "Iteration: ", *arr)

if __name__ == "__main__":
    arr = [2, 6, 8, 12, 45, 21, 1, 3, 49, 7]
    print("Array before sorting: ", *arr)
    selectionSort(arr, len(arr))
    print("Array after Selection sort: ", *arr)