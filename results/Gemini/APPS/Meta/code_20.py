def solve():
    s = input()
    hh = int(s[:2])
    mm = int(s[3:])
    
    count = 0
    while True:
        h_str = str(hh).zfill(2)
        m_str = str(mm).zfill(2)
        
        if h_str == m_str[::-1]:
            print(count)
            return
        
        mm += 1
        if mm == 60:
            mm = 0
            hh += 1
            if hh == 24:
                hh = 0
        
        count += 1

solve()