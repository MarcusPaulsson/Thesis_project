def is_palindrome(time_str):
    return time_str == time_str[::-1]

def next_palindrome_time(hh, mm):
    minutes_passed = 0
    while True:
        mm += 1
        if mm == 60:
            mm = 0
            hh += 1
            if hh == 24:
                hh = 0
        minutes_passed += 1
        
        time_str = f"{hh:02}:{mm:02}"
        if is_palindrome(time_str):
            return minutes_passed

def min_minutes_to_palindrome(time):
    hh, mm = map(int, time.split(':'))
    return next_palindrome_time(hh, mm)

# Sample input
time_input = input().strip()
print(min_minutes_to_palindrome(time_input))