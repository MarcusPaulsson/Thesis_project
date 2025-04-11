def solve():
    n = int(input())
    
    min_days_off = (n // 7) * 2
    rem = n % 7
    
    if rem == 6:
        min_days_off += 1
    
    max_days_off = (n // 7) * 2 + min(2, rem)
    
    print(min_days_off, max_days_off)

solve()