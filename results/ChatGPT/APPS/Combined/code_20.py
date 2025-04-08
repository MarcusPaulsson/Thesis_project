def is_palindrome(time):
    return time == time[::-1]

def increment_time(hh, mm):
    mm += 1
    if mm == 60:
        mm = 0
        hh += 1
        if hh == 24:
            hh = 0
    return hh, mm

def minutes_until_palindrome(start_time):
    hh, mm = map(int, start_time.split(':'))
    count = 0
    
    while not is_palindrome(f"{hh:02}:{mm:02}"):
        hh, mm = increment_time(hh, mm)
        count += 1
        
    return count

# Input reading
input_time = input().strip()
# Calculate and print the result
print(minutes_until_palindrome(input_time))