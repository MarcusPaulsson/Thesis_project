def solve():
    x = int(input())
    hh, mm = map(int, input().split())

    def is_lucky(h, m):
        return '7' in str(h) or '7' in str(m)

    count = 0
    current_hh = hh
    current_mm = mm

    while not is_lucky(current_hh, current_mm):
        current_mm -= x
        if current_mm < 0:
            current_mm += 60
            current_hh -= 1
            if current_hh < 0:
                current_hh += 24
        count += 1

    print(count)

solve()