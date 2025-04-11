def solve():
    x = int(input())
    hh, mm = map(int, input().split())

    def is_lucky(h, m):
        return '7' in str(h) or '7' in str(m)

    count = 0
    current_h = hh
    current_m = mm

    while True:
        if is_lucky(current_h, current_m):
            print(count)
            return

        current_m -= x
        if current_m < 0:
            current_m += 60
            current_h -= 1
            if current_h < 0:
                current_h += 24
        count += 1

solve()