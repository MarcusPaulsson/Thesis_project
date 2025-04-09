def solve():
    n = int(input())
    
    def is_lucky(year):
        s = str(year)
        non_zero_count = 0
        for digit in s:
            if digit != '0':
                non_zero_count += 1
        return non_zero_count <= 1

    year = n + 1
    while True:
        if is_lucky(year):
            print(year - n)
            return
        year += 1

solve()