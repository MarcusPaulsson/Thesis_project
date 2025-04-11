def solve():
    s = input()
    hh = int(s[:2])
    mm = int(s[3:])
    
    ans = float('inf')
    
    for h in range(24):
        for m in range(60):
            h_str = str(h).zfill(2)
            m_str = str(m).zfill(2)
            
            if h_str == m_str[::-1]:
                curr_minutes = hh * 60 + mm
                target_minutes = h * 60 + m
                
                diff = (target_minutes - curr_minutes) % (24 * 60)
                ans = min(ans, diff)
                
    print(ans)

solve()