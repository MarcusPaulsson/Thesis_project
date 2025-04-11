def next_lucky_year(current_year):
    # Increment the year until we find a lucky year
    while True:
        current_year += 1
        if is_lucky_year(current_year):
            return current_year - (current_year - 1)

def is_lucky_year(year):
    # Convert year to string and count non-zero digits
    return sum(1 for digit in str(year) if digit != '0') <= 1

# Read input
n = int(input())
# Output the result
print(next_lucky_year(n))