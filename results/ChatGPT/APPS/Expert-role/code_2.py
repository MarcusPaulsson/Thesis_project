def next_lucky_year(n):
    while True:
        n += 1
        if str(n).count('0') + len(set(str(n))) - 1 <= 1:
            return n - (n - 1)

current_year = int(input())
print(next_lucky_year(current_year))