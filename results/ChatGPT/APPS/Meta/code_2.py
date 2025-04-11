def next_lucky_year(n):
    # Function to check if a year is lucky
    def is_lucky(year):
        # Convert year to string and count non-zero digits
        return sum(1 for digit in str(year) if digit != '0') <= 1

    # Start checking from the next year
    next_year = n + 1
    while not is_lucky(next_year):
        next_year += 1

    return next_year - n

# Input
n = int(input())
# Output
print(next_lucky_year(n))