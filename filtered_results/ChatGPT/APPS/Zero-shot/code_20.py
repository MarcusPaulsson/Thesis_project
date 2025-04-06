def is_palindrome_time(hh, mm):
    return f"{hh:02}:{mm:02}" == f"{hh:02}:{mm:02}"[::-1]

def next_palindrome_time(hh, mm):
    minutes_passed = 0
    while not is_palindrome_time(hh, mm):
        mm += 1
        minutes_passed += 1
        if mm == 60:
            mm = 0
            hh += 1
            if hh == 24:
                hh = 0
    return minutes_passed

time_input = input().strip()
hh, mm = map(int, time_input.split(':'))
result = next_palindrome_time(hh, mm)
print(result)