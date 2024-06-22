def checkRoot(m, n, val):
    ans = 1
    for _ in range(n):
        ans *= m
        if ans > val:
            return 2
    if ans == val:
        return 1
    return 0

def NthRoot(n, val):
    l, r = 0, val
    while l <= r:
        m = (l + r) // 2
        decision = checkRoot(m, n, val)
        if decision == 1:
            return m
        elif not decision:
            l = m + 1
        else:
            r = m - 1
    return -1

if __name__ == "__main__":
    val = int(input("Enter a number: "))
    n = int(input("Enter root you want to calculate: "))
    print(NthRoot(n, val))