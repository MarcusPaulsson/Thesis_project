def is_lucky_year(year):
    """Check if a year is lucky (has no more than one non-zero digit)."""
    non_zero_digits = sum(1 for digit in str(year) if digit != '0')
    return non_zero_digits <= 1

def next_lucky_year(current_year):
    """Find the next lucky year after the given current year."""
    next_year = current_year + 1
    while not is_lucky_year(next_year):
        next_year += 1
    return next_year - current_year

def main():
    # Input
    current_year = int(input())
    
    # Output the number of years until the next lucky year
    print(next_lucky_year(current_year))

if __name__ == "__main__":
    main()