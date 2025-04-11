def is_lucky_year(year):
    """Check if the year is lucky (has at most one non-zero digit)."""
    non_zero_digits = sum(1 for digit in str(year) if digit != '0')
    return non_zero_digits <= 1

def next_lucky_year(current_year):
    """Find the next lucky year after the current year."""
    next_year = current_year + 1
    while not is_lucky_year(next_year):
        next_year += 1
    return next_year - current_year

# Input
n = int(input().strip())
# Output
print(next_lucky_year(n))