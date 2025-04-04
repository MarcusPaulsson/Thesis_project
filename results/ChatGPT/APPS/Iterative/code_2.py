def is_lucky_year(year):
    return str(year).count('0') <= 1

n = int(input("Enter a year: "))
next_year = n + 1

while not is_lucky_year(next_year):
    next_year += 1

print(next_year - n)