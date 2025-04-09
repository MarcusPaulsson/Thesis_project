def next_lucky_year(n):
    while True:
        n += 1
        if sum(1 for digit in str(n) if digit != '0') <= 1:
            return n - (n - 1)

current_year = int(input())
print(next_lucky_year(current_year))