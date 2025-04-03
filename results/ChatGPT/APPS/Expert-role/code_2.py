def next_lucky_year(n):
    # Increment the year until we find the next lucky year
    while True:
        n += 1
        # Convert the year to string and check the number of non-zero digits
        if sum(1 for digit in str(n) if digit != '0') <= 1:
            return n - (n - 1)

# Read input
current_year = int(input().strip())
# Print the number of years until the next lucky year
print(next_lucky_year(current_year))