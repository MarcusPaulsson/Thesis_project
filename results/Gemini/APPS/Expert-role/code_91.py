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
            
            ti = 0
            for k in range(len(temp)):
                if ti < m and temp[k] == t[ti]:
                    ti += 1
            
            if ti == m:
                ans = max(ans, j - i)
                
    print(ans)
    
solve()