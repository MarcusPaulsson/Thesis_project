def solve():
    n = int(input())
    
    full_weeks = n // 7
    remaining_days = n % 7
    
    min_days_off = full_weeks * 2
    max_days_off = full_weeks * 2
    
    if remaining_days == 6:
        min_days_off += 1
    elif remaining_days >= 1:
        pass
        
    max_days_off += min(remaining_days, 2)
    
    print(min_days_off, max_days_off)

solve()