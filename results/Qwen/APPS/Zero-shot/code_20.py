def next_palindrome_time(current_time):
    hh, mm = map(int, current_time.split(':'))
    while True:
        mm += 1
        if mm == 60:
            hh += 1
            mm = 0
            if hh == 24:
                hh = 0
        time_str = f"{hh:02}:{mm:02}"
        if time_str == time_str[::-1]:
            return mm - int(current_time.split(':')[1])

current_time = input()
print(next_palindrome_time(current_time))