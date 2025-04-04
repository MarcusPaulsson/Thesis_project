def is_palindrome(time):
    return time == time[::-1]

def time_to_palindrome(hh, mm):
    minutes_passed = 0
    while True:
        if is_palindrome(f"{hh:02}:{mm:02}"):
            return minutes_passed
        mm += 1
        if mm == 60:
            mm = 0
            hh += 1
            if hh == 24:
                hh = 0
        minutes_passed += 1

current_time = input().strip()
hh, mm = map(int, current_time.split(':'))
result = time_to_palindrome(hh, mm)
print(result)