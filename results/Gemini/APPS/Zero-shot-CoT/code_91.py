def solve():
    s = input()
    t = input()
    n = len(s)
    m = len(t)
    ans = 0
    for i in range(n + 1):
        for j in range(i, n + 1):
            temp = ""
            if i > 0:
                temp += s[:i]
            if j < n:
                temp += s[j:]
            
            k = 0
            l = 0
            while k < len(temp) and l < m:
                if temp[k] == t[l]:
                    l += 1
                k += 1
            
            if l == m:
                ans = max(ans, j - i)
    print(ans)

solve()