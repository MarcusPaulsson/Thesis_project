def is_palindrome(time):
    return time == time[::-1]

def add_minutes(hh, mm, minutes):
    mm += minutes
    hh += mm // 60
    mm %= 60
    hh %= 24
    return hh, mm

def minimum_sleep_minutes(current_time):
    hh, mm = map(int, current_time.split(':'))
    minutes = 0
    
    while True:
        formatted_time = f"{hh:02d}:{mm:02d}"
        if is_palindrome(formatted_time):
            return minutes
        minutes += 1
        hh, mm = add_minutes(hh, mm, 1)

current_time = input().strip()
print(minimum_sleep_minutes(current_time))