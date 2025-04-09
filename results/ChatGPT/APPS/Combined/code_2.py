def is_lucky_year(year):
    """Check if a year is lucky based on the number of non-zero digits."""
    non_zero_count = sum(1 for digit in str(year) if digit != '0')
    return non_zero_count <= 1

def next_lucky_year(current_year):
    """Find the next lucky year after the current year."""
    next_year = current_year + 1
    while not is_lucky_year(next_year):
        next_year += 1
    return next_year - current_year

if __name__ == "__main__":
    n = int(input().strip())
    print(next_lucky_year(n))