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

def minutes_to_palindrome(time):
    hh, mm = map(int, time.split(':'))
    minutes = 0
    while True:
        if is_palindrome(f"{hh:02}:{mm:02}"):
            return minutes
        mm += 1
        minutes += 1
        if mm == 60:
            mm = 0
            hh += 1
            if hh == 24:
                hh = 0

time_input = input().strip()
print(minutes_to_palindrome(time_input))