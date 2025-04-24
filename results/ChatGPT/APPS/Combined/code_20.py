def is_palindrome(time_str):
    return time_str == time_str[::-1]

def increment_time(hh, mm):
    mm += 1
    if mm == 60:
        mm = 0
        hh += 1
        if hh == 24:
            hh = 0
    return hh, mm

def minutes_until_palindrome(current_time):
    hh, mm = map(int, current_time.split(':'))
    minutes = 0
    
    while not is_palindrome(f"{hh:02}:{mm:02}"):
        hh, mm = increment_time(hh, mm)
        minutes += 1
        
    return minutes

if __name__ == "__main__":
    current_time = input().strip()
    print(minutes_until_palindrome(current_time))