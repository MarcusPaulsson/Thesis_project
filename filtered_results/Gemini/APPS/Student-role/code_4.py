def solve():
    x = int(input())
    hh, mm = map(int, input().split())
    
    count = 0
    while True:
        h_str = str(hh).zfill(2)
        m_str = str(mm).zfill(2)
        
        if '7' in h_str or '7' in m_str:
            print(count)
            return
        
        minutes = hh * 60 + mm
        minutes -= x
        
        if minutes < 0:
            minutes += 24 * 60
            
        hh = minutes // 60 % 24
        mm = minutes % 60
        
        count += 1

solve()