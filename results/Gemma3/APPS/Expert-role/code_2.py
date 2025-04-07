def solve():
    n = int(input())
    
    def is_lucky(year):
        s = str(year)
        count = 0
        for digit in s:
            if digit != '0':
                count += 1
        return count <= 1
    
    year = n + 1
    while True:
        if is_lucky(year):
            print(year - n)
            return
        year += 1

solve()