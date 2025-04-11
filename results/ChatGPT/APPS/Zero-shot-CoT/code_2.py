n = int(input())

def is_lucky(year):
    return str(year).count('0') + len(set(str(year))) <= 2

next_year = n + 1
while not is_lucky(next_year):
    next_year += 1

print(next_year - n)