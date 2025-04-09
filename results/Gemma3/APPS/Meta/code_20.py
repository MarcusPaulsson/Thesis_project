def solve():
    time_str = input()
    hours, minutes = map(int, time_str.split(':'))
    
    def is_palindrome(h, m):
        h_str = str(h).zfill(2)
        m_str = str(m).zfill(2)
        return h_str == m_str[::-1]
    
    min_sleep_time = float('inf')
    
    # Check current time
    if is_palindrome(hours, minutes):
        print(0)
        return
    
    # Find next palindrome
    current_minutes = hours * 60 + minutes
    
    for i in range(1, 1441):
        next_minutes = current_minutes + i
        next_hours = (next_minutes // 60) % 24
        next_minutes %= 60
        
        if is_palindrome(next_hours, next_minutes):
            min_sleep_time = i
            break
            
    print(min_sleep_time)

solve()