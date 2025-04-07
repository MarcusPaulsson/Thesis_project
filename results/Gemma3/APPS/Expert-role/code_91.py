def solve():
    s = input()
    t = input()
    n = len(s)
    m = len(t)
    
    max_len = 0
    
    for l in range(n):
        for r in range(l, n):
            temp_s = s[:l] + s[r+1:]
            
            t_idx = 0
            temp_s_idx = 0
            
            while t_idx < m and temp_s_idx < len(temp_s):
                if t[t_idx] == temp_s[temp_s_idx]:
                    t_idx += 1
                temp_s_idx += 1
            
            if t_idx == m:
                max_len = max(max_len, r - l + 1)
                
    print(max_len)

solve()