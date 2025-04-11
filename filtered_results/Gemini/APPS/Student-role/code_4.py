def solve():
    x = int(input())
    hh, mm = map(int, input().split())
    
    count = 0
    curr_hh = hh
    curr_mm = mm
    
    while True:
        time_str = "{:02d}:{:02d}".format(curr_hh, curr_mm)
        if '7' in time_str:
            print(count)
            return
        
        curr_mm -= x
        if curr_mm < 0:
            curr_hh -= 1
            curr_mm += 60
            if curr_hh < 0:
                curr_hh += 24
        
        count += 1

solve()