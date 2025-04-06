def solve():
    n = int(input())
    
    min_days_off = (n // 7) * 2
    rem = n % 7
    
    if rem >= 5:
        min_days_off += (rem - 4)
    
    max_days_off = (n // 7) * 2
    
    max_days_off += min(2, rem)
        
    print(min_days_off, max_days_off)

solve()