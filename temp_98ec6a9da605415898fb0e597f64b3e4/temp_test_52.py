n = int(input())

def is_lucky_year(year):
    digits = str(year)
    non_zero_digits = [d for d in digits if d != '0']
    return len(non_zero_digits) <= 1

next_year = n + 1
while not is_lucky_year(next_year):
    next_year += 1

print(next_year - n)