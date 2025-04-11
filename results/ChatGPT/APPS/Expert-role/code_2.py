n = int(input())

def is_lucky_year(year):
    non_zero_digits = sum(1 for digit in str(year) if digit != '0')
    return non_zero_digits <= 1

next_year = n + 1
while not is_lucky_year(next_year):
    next_year += 1

print(next_year - n)