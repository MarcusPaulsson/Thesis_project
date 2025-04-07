n = int(input())

def is_lucky(year):
    # Count non-zero digits
    non_zero_count = sum(1 for digit in str(year) if digit != '0')
    return non_zero_count <= 1

next_year = n + 1
while not is_lucky(next_year):
    next_year += 1

print(next_year - n)