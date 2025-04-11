n = int(input())

def is_lucky(year):
    return len(set(str(year)) - {'0'}) <= 1

next_year = n + 1
while not is_lucky(next_year):
    next_year += 1

print(next_year - n)