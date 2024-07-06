def bubbleSort(arr):
    for i in range(len(arr)):
        for j in range(len(arr) - 1 - i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
        print(i + 1, "Iteration: ", *arr)
    pass

def optimizedBubbleSort(arr):
    for i in range(len(arr)):
        swapped = False
        for j in range(len(arr) - 1 - i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        print(i + 1, "Iteration: ", *arr)
        if not swapped:
            break
    pass

if __name__ == "__main__":
    arr = [2, 6, 8, 12, 45, 21, 1, 3, 49, 7]
    print("Array before sorting: ", *arr)
    optimizedBubbleSort(arr)
    print("Array after bubble sort: ", *arr)
    bubbleSort(arr)
    print("Array after bubble sort: ", *arr)