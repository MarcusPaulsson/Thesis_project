def solve():
    x = int(input())
    hh, mm = map(int, input().split())

    def is_lucky(h, m):
        return '7' in str(h) or '7' in str(m)

    count = 0
    while True:
        if is_lucky(hh, mm):
            print(count)
            return

        minutes = hh * 60 + mm
        minutes -= x
        if minutes < 0:
            minutes += 24 * 60

        hh = minutes // 60 % 24
        mm = minutes % 60
        
        count += 1

solve()