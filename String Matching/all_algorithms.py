def naive_approach(pattern, text):
    n = len(text)
    m = len(pattern)
    ans = []
    for i in range(n - m + 1):
        j = 0
        while j < m and text[i + j] == pattern[j]:
            j += 1
        if j == m:
           ans.append(i)
    return ans


def KMP(pat, txt):
    M = len(pat)
    N = len(txt)
    lps = computeLPSArray(pat, M)
    print("LPS array of pattern: ", lps)
    ans = []
    i = 0
    j = 0
    while (N - i) >= (M - j):
        if pat[j] == txt[i]:
            i += 1
            j += 1
 
        if j == M:
            ans.append(i-j)
            j = lps[j-1]
        elif i < N and pat[j] != txt[i]:
            if j != 0:
                j = lps[j-1]
            else:
                i += 1
    return ans
def computeLPSArray(pat, M):
    len = 0
    lps = [0] * M
    i = 1
    while i < M:
        if pat[i] == pat[len]:
            len += 1
            lps[i] = len
            i += 1
        else:
            if len != 0:
                len = lps[len-1]
            else:
                lps[i] = 0
                i += 1
    return lps


res1 = naive_approach("aaba", "aabaacaadaabaaba")
print(res1)
print(KMP("aaacaaaaac", "aabaacaadaabaaba"))