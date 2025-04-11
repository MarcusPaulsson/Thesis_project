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
            return time_str

def minutes_to_palindrome(current_time):
    hh, mm = map(int, current_time.split(':'))
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

if __name__ == "__main__":
    current_time = input().strip()
    print(minutes_to_palindrome(current_time))