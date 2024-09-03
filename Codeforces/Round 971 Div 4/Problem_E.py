t = int(input())
for _ in range(t):
    n, k = [int(s) for s in input().split()]
    lidx = k
    ridx = n + k - 1
    lsum = ((lidx - 1) * lidx) // 2
    rsum = ((ridx + 1) * ridx) // 2
    ans = rsum - lsum
    cnt = 0
    seta = set()
    while lidx <= ridx:
        if (lidx, ridx) in seta:
            break
        seta.add((lidx, ridx))
        midx = (lidx + ridx) // 2
        msum = ((midx + 1) * midx) // 2
        p1 = msum - lsum
        p2 = rsum - msum
        if p1 < p2:
            lidx = midx  
        elif p1 > p2:
            ridx = midx
        else:
            ans = 0
            break
        ans = min(ans, abs(p1 - p2))
    print(ans)