def solve():
    n = int(input())
    
    min_days_off = (n // 7) * 2
    max_days_off = (n // 7) * 2
    
    remaining_days = n % 7
    
    if remaining_days >= 5:
        max_days_off += 2
    elif remaining_days >= 3:
        max_days_off += 1
    
    if n < 7:
        min_days_off = 0
        max_days_off = min(n, 2)
    
    print(min_days_off, max_days_off)

solve()