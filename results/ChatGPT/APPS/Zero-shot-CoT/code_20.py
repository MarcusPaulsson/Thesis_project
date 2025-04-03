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
        time = f"{hh:02}:{mm:02}"
        if is_palindrome(time):
            return time

def min_minutes_to_palindrome(current_time):
    hh, mm = map(int, current_time.split(':'))
    minutes = 0
    
    while True:
        if is_palindrome(f"{hh:02}:{mm:02}"):
            return minutes
        minutes += 1
        mm += 1
        if mm == 60:
            mm = 0
            hh += 1
            if hh == 24:
                hh = 0

# Input
current_time = input().strip()
# Output
print(min_minutes_to_palindrome(current_time))