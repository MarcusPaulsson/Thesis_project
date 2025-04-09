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

        mm -= x
        if mm < 0:
            mm += 60
            hh -= 1
            if hh < 0:
                hh += 24
        count += 1

solve()