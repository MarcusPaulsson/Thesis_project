def is_palindrome(time):
    return time == time[::-1]

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

time_input = input().strip()
hh, mm = map(int, time_input.split(':'))
result = next_palindrome_time(hh, mm)
print(result)