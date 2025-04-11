def is_palindrome(time_str):
    return time_str == time_str[::-1]

def next_palindrome_time(hh, mm):
    while True:
        mm += 1
        if mm == 60:
            mm = 0
            hh += 1
            if hh == 24:
                hh = 0
        
        time_str = f"{hh:02}:{mm:02}"
        if is_palindrome(time_str):
            return (hh, mm)

def min_sleep_minutes(current_time):
    hh, mm = map(int, current_time.split(':'))
    target_hh, target_mm = next_palindrome_time(hh, mm)
    
    # Calculate the difference in minutes
    minutes_passed = (target_hh * 60 + target_mm) - (hh * 60 + mm)
    return minutes_passed if minutes_passed >= 0 else minutes_passed + 1440

# Input
current_time = input().strip()
# Output
print(min_sleep_minutes(current_time))