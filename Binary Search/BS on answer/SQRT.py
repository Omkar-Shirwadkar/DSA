def mySqrt(n):
    l, r = 0, n
    while l <= r:
        m = (l + r) // 2
        if m * m <= n:
            l = m + 1
        else:
            r = m - 1
    return r


if __name__ == "__main__":
    n = int(input("Enter a number to calculate square root: "))
    print("Square root of the number: ", mySqrt(n))