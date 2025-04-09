def next_lucky_year(n):
    # Function to check if a year is lucky
    def is_lucky(year):
        non_zero_digits = [digit for digit in str(year) if digit != '0']
        return len(non_zero_digits) <= 1

    # Start checking from the next year
    years_waited = 0
    while True:
        n += 1
        years_waited += 1
        if is_lucky(n):
            return years_waited

# Input
n = int(input().strip())
# Output
print(next_lucky_year(n))