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
            return hh, mm

def minutes_until_palindrome(hh, mm):
    start_time = (hh, mm)
    target_time = next_palindrome_time(hh, mm)
    
    start_minutes = start_time[0] * 60 + start_time[1]
    target_minutes = target_time[0] * 60 + target_time[1]
    
    return (target_minutes - start_minutes) % (24 * 60)

# Read input
input_time = input().strip()
hh, mm = map(int, input_time.split(':'))

# Get the result
result = minutes_until_palindrome(hh, mm)
print(result)