def solve():
    h1, m1 = map(int, input().split(':'))
    h2, m2 = map(int, input().split(':'))
    
    total_minutes = (h2 * 60 + m2) - (h1 * 60 + m1)
    
    mid_minutes = (h1 * 60 + m1) + (total_minutes // 2)
    
    h3 = (mid_minutes // 60) % 24
    m3 = mid_minutes % 60
    
    print(f"{h3:02}:{m3:02}")

solve()