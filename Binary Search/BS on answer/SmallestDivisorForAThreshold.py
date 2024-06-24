import math

def smallestDivisor(arr, threshold):
    l, r = 1, max(arr)
    while l <= r:
        m = (l + r) // 2
        currdiv = 0
        for i in arr:
            currdiv += math.ceil(i / m)
        if currdiv <= threshold:
            r = m - 1
        else:
            l = m + 1
    return l

if __name__ == "__main__":
    arr = [44,22,33,11,1]
    threshold = 5
    print("Smallest divisor dividing the array less than threshold: ", smallestDivisor(arr, threshold))