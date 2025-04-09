def next_lucky_year(n):
    # Increment the year until we find a lucky year
    while True:
        n += 1
        # Convert the year to a string to check its digits
        digits = str(n)
        # Count non-zero digits
        non_zero_count = sum(1 for digit in digits if digit != '0')
        # Check if the year is lucky
        if non_zero_count <= 1:
            return n - (n - 1)  # Return the difference between the current year and the next lucky year

# Read input
current_year = int(input())
# Output the result
print(next_lucky_year(current_year))