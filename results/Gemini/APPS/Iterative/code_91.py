def solve():
    s = input()
    t = input()
    n = len(s)
    m = len(t)
    
    ans = 0
    for i in range(n + 1):
        for j in range(i, n + 1):
            temp_s = ""
            if i > 0:
                temp_s += s[:i]
            if j < n:
                temp_s += s[j:]
            
            k = 0
            l = 0
            
            while k < len(temp_s) and l < m:
                if temp_s[k] == t[l]:
                    l += 1
                k += 1
            
            if l == m:
                ans = max(ans, j - i)
    
    print(ans)

solve()