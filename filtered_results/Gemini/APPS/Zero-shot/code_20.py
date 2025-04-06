def solve():
    s = input()
    hh = int(s[:2])
    mm = int(s[3:])
    
    ans = float('inf')
    
    for i in range(24 * 60):
        curr_hh = hh
        curr_mm = mm
        
        time_str = "{:02d}:{:02d}".format(curr_hh, curr_mm)
        
        if time_str[0] == time_str[4] and time_str[1] == time_str[3]:
            ans = min(ans, i)
            
        mm += 1
        if mm == 60:
            mm = 0
            hh += 1
            if hh == 24:
                hh = 0
                
    print(ans)

solve()