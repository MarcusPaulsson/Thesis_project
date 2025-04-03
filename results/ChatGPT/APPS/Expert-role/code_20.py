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
        current_time = f"{hh:02}:{mm:02}"
        if is_palindrome(current_time):
            return hh, mm

def minutes_until_palindrome(current_time):
    hh, mm = map(int, current_time.split(':'))
    count = 0
    while not is_palindrome(f"{hh:02}:{mm:02}"):
        mm += 1
        count += 1
        if mm == 60:
            mm = 0
            hh += 1
            if hh == 24:
                hh = 0
    return count

# Read input
current_time = input().strip()
# Calculate and print the result
print(minutes_until_palindrome(current_time))