def next_lucky_year(n):
    n += 1
    while True:
        if sum(int(digit) != 0 for digit in str(n)) > 1:
            n += 1
        else:
            return n - 1

n = int(input())
print(next_lucky_year(n))