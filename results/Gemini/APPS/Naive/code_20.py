def is_palindrome(time_str):
    return time_str == time_str[::-1]

def solve():
    time_str = input()
    hh = int(time_str[:2])
    mm = int(time_str[3:])
    
    minutes = 0
    while True:
        time_str = "{:02d}:{:02d}".format(hh, mm)
        if is_palindrome(time_str):
            print(minutes)
            return
        
        minutes += 1
        mm += 1
        if mm == 60:
            mm = 0
            hh += 1
            if hh == 24:
                hh = 0

solve()