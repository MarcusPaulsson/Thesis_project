def next_lucky_year(current_year):
    # Increment the year until we find a lucky year
    while True:
        current_year += 1
        # Convert the year to string and count non-zero digits
        if sum(1 for digit in str(current_year) if digit != '0') <= 1:
            return current_year - (current_year - 1)

# Read input
n = int(input().strip())
# Get the result
result = next_lucky_year(n)
# Print the result
print(result)