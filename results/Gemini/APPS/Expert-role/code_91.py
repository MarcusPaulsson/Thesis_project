def solve():
    s = input()
    t = input()
    n = len(s)
    m = len(t)
    
    max_len = 0
    
    for i in range(n + 1):
        for j in range(i, n + 1):
            temp_s = ""
            if i > 0:
                temp_s += s[:i]
            if j < n:
                temp_s += s[j:]
            
            
            
            t_idx = 0
            temp_s_idx = 0
            
            possible = True
            while t_idx < m and temp_s_idx < len(temp_s):
                if t[t_idx] == temp_s[temp_s_idx]:
                    t_idx += 1
                temp_s_idx += 1
            
            if t_idx == m:
                max_len = max(max_len, j - i)
    
    print(max_len)

solve()