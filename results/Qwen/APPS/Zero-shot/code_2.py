def next_lucky_year(n):
    n += 1
    while True:
        if len([int(digit) for digit in str(n) if int(digit) != 0]) <= 1:
            return n - 1
        n += 1

n = int(input())
print(next_lucky_year(n))