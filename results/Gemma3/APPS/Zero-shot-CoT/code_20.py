def solve():
    s = input()
    h, m = map(int, s.split(':'))
    
    def is_palindrome(time_str):
        return time_str == time_str[::-1]
    
    current_time = h * 60 + m
    
    min_minutes = float('inf')
    
    for i in range(1440):
        next_time = (current_time + i) % (24 * 60)
        next_h = next_time // 60
        next_m = next_time % 60
        
        next_h_str = str(next_h).zfill(2)
        next_m_str = str(next_m).zfill(2)
        
        next_time_str = next_h_str + next_m_str
        
        if is_palindrome(next_time_str):
            min_minutes = min(min_minutes, i)
            
    print(min_minutes)

solve()