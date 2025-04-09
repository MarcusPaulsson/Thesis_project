def is_palindrome(time):
    return time == time[::-1]

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
            return time_str

def min_minutes_to_palindrome(current_time):
    hh, mm = map(int, current_time.split(":"))
    minutes = 0
    while True:
        palindrome_time = next_palindrome_time(hh, mm)
        if palindrome_time == f"{hh:02}:{mm:02}":
            return minutes
        minutes += 1
        mm += 1
        if mm == 60:
            mm = 0
            hh += 1
            if hh == 24:
                hh = 0

current_time = input().strip()
print(min_minutes_to_palindrome(current_time))