def solve():
    n = int(input())
    
    weeks = n // 7
    remaining_days = n % 7
    
    min_days_off = weeks * 2
    max_days_off = weeks * 2
    
    if remaining_days == 1:
        min_days_off += 0
        max_days_off += 1
    elif remaining_days == 2:
        min_days_off += 0
        max_days_off += 2
    elif remaining_days == 3:
        min_days_off += 0
        max_days_off += 2
    elif remaining_days == 4:
        min_days_off += 0
        max_days_off += 2
    elif remaining_days == 5:
        min_days_off += 0
        max_days_off += 2
    elif remaining_days == 6:
        min_days_off += 1
        max_days_off += 2

    print(min_days_off, max_days_off)

solve()