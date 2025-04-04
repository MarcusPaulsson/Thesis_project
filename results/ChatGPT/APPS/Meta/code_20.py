def is_palindrome(time):
    return time == time[::-1]

def next_palindrome_time(hh, mm):
    minutes_passed = 0
    while True:
        mm += 1
        if mm == 60:
            mm = 0
            hh += 1
            if hh == 24:
                hh = 0
        minutes_passed += 1
        current_time = f"{hh:02}:{mm:02}"
        if is_palindrome(current_time):
            return minutes_passed

# Read input
input_time = input().strip()
hh, mm = map(int, input_time.split(':'))

# Get the result
result = next_palindrome_time(hh, mm)

# Output the result
print(result)