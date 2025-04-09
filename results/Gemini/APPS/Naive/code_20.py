def solve():
    time_str = input()
    hh = int(time_str[:2])
    mm = int(time_str[3:])
    
    minutes = 0
    while True:
        hh_str = str(hh).zfill(2)
        mm_str = str(mm).zfill(2)
        
        if hh_str == mm_str[::-1]:
            print(minutes)
            return
        
        mm += 1
        if mm == 60:
            mm = 0
            hh += 1
            if hh == 24:
                hh = 0
        minutes += 1

solve()