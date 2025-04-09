def solve():
    s = input()
    hh = int(s[:2])
    mm = int(s[3:])
    
    ans = float('inf')
    
    for i in range(24 * 60):
        cur_hh = hh
        cur_mm = mm
        
        time_str = "{:02d}:{:02d}".format(cur_hh, cur_mm)
        
        if time_str == time_str[::-1]:
            ans = min(ans, i)
            break
        
        mm += 1
        if mm == 60:
            mm = 0
            hh += 1
            if hh == 24:
                hh = 0
            
    print(ans)

solve()