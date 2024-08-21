def make_equal(arr1, arr2, n):
    if len(arr1) != len(arr2):
        return -1
    arr1.sort()
    arr2.sort()
    nary = {}
    for i in range(n):
        if arr1[i] in nary:
            nary[arr1[i]] += 1
        else:
            nary[arr1[i]] = 1
        if arr2[i] in nary:
            nary[arr2[i]] += 1
        else:
            nary[arr2[i]] = 1
    for i in nary.values():
        if i & 1:
            return -1
    ans = 0
    l1, l2, r1, r2 = 0, 0, n - 1, n - 1
    while True:
        l1clutch = l2clutch = False
        
        while arr1[l1] == arr2[l2]:
            l1 += 1
            l2 += 1
            
        if l1 > r1 or l2 > r2:
            break
        
        if arr1[l1] < arr2[l2]:
            l1clutch = True
            ans += arr1[l1]
            l1 += 2
        else:
            l2clutch = True
            ans += arr2[l2]
            l2 += 2
            
        if l1 > r1 or l2 > r2:
            break
        
        while arr1[r1] == arr2[r2]:
            r1 -= 1
            r2 -= 1
        
        if l1 > r1 or l2 > r2:
            break
        
        if l1clutch:
            r2 -= 2
        elif l2clutch:
            r1 -= 2
        if l1 > r1 or l2 > r2:
            break
    return ans
a1 = [4,4,4,4]
a2 = [2,2,5,5]
n = 4
ans1 = make_equal(a1, a2,4)
b1 = [2,2,2,4]
b2 = [1,1,2,4]
ans2 = make_equal(b1, b2,4)
print(ans1, ans2)