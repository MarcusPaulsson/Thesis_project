n = int(input())

def is_lucky(year):
    count = 0
    while year > 0:
        if year % 10 != 0:
            count += 1
        year //= 10
    return count <= 1

current_year = n
while True:
    current_year += 1
    if is_lucky(current_year):
        print(current_year - n)
        break