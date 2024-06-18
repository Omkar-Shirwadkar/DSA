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


res1 = naive_approach("aaba", "aabaacaadaabaaba")
print(res1)