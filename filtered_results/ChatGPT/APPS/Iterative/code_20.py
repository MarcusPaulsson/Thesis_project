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

def time_difference(hh1, mm1, hh2, mm2):
    return (hh2 * 60 + mm2) - (hh1 * 60 + mm1)

current_time = input().strip()
hh, mm = map(int, current_time.split(':'))
next_hh, next_mm = next_palindrome_time(hh, mm)
result = time_difference(hh, mm, next_hh, next_mm)
print(result)