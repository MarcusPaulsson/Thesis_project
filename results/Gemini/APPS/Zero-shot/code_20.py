def solve():
    s = input()
    hh = int(s[:2])
    mm = int(s[3:])
    
    ans = float('inf')
    
    for i in range(24 * 60):
        curr_hh = hh
        curr_mm = mm
        
        time_str = "{:02d}:{:02d}".format(curr_hh, curr_mm)
        
        if time_str == time_str[::-1]:
            ans = 0
            break
            
        
        new_mm = (mm + 1) % 60
        new_hh = hh + (mm + 1) // 60
        
        hh = new_hh % 24
        mm = new_mm
        
    else:
        hh = int(s[:2])
        mm = int(s[3:])
        
        for i in range(24 * 60):
            curr_hh = hh
            curr_mm = mm

            time_str = "{:02d}:{:02d}".format(curr_hh, curr_mm)

            if time_str == time_str[::-1]:
                ans = i
                break


            new_mm = (mm + 1) % 60
            new_hh = hh + (mm + 1) // 60

            hh = new_hh % 24
            mm = new_mm
        
    print(ans)
    

solve()