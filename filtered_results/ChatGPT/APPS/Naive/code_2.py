def next_lucky_year(current_year):
    def is_lucky(year):
        non_zero_digits = [digit for digit in str(year) if digit != '0']
        return len(non_zero_digits) <= 1

    next_year = current_year + 1
    while not is_lucky(next_year):
        next_year += 1
    
    return next_year - current_year

# Input
n = int(input().strip())
# Output
print(next_lucky_year(n))