n = int(input())

def next_lucky_year(year):
    while True:
        year += 1
        if str(year).count('0') == len(str(year)) - 1 and str(year).count('1') + str(year).count('2') + str(year).count('3') + str(year).count('4') + str(year).count('5') + str(year).count('6') + str(year).count('7') + str(year).count('8') + str(year).count('9') == 1:
            return year

next_year = next_lucky_year(n)
print(next_year - n)