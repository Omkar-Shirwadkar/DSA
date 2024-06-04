def brute(s):
    n = len(s)
    maxlen = 0
    for i in range(n):
        hasharr = [0] * 256
        for j in range(i, n):
            if hasharr[ord(s[j])] == 1:
                break
            currlen = j - i + 1
            maxlen = max(currlen, maxlen)
            hasharr[ord(s[j])] = 1
    return maxlen

def optimal(s):
    n = len(s)
    l = r = maxlen = 0
    hasharr = [-1] * 256
    while r < n:
        if hasharr[ord(s[r])] != -1:
            if hasharr[ord(s[r])] >= l:
                l = hasharr[ord(s[r])] + 1
        currlen = r - l + 1
        maxlen = max(maxlen, currlen)
        hasharr[ord(s[r])] = r
        r += 1
    return maxlen

t = int(input())
for _ in range(t):
    s = input()
    print(brute(s))
    print(optimal(s))