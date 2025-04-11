def next_lucky_year(n):
    # Function to check if a year is lucky
    def is_lucky(year):
        return str(year).count('0') + len(set(str(year))) <= 2

    # Increment the year until we find the next lucky year
    while True:
        n += 1
        if is_lucky(n):
            return n - (n - 1)

# Read input
current_year = int(input())
# Output the result
print(next_lucky_year(current_year))