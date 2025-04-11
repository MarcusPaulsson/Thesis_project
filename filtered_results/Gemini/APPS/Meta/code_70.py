def solve():
    start_time = input()
    end_time = input()
    
    start_h, start_m = map(int, start_time.split(':'))
    end_h, end_m = map(int, end_time.split(':'))
    
    start_minutes = start_h * 60 + start_m
    end_minutes = end_h * 60 + end_m
    
    mid_minutes = (start_minutes + end_minutes) // 2
    
    mid_h = mid_minutes // 60
    mid_m = mid_minutes % 60
    
    print(f"{mid_h:02}:{mid_m:02}")

solve()