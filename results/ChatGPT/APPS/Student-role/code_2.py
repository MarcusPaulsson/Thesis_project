n = int(input())

def next_lucky_year(year):
    while True:
        year += 1
        if str(year).count('0') == len(str(year)) - 1 and str(year).count('1') <= 1:
            return year

next_year = next_lucky_year(n)
print(next_year - n)