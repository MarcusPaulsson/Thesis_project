n = int(input())

def next_lucky_year(current_year):
    while True:
        current_year += 1
        if str(current_year).count('0') + len(set(str(current_year))) - 1 <= 1:
            return current_year

next_year = next_lucky_year(n)
print(next_year - n)