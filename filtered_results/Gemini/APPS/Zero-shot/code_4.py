def solve():
    x = int(input())
    hh, mm = map(int, input().split())

    count = 0
    while True:
        h_str = str(hh).zfill(2)
        m_str = str(mm).zfill(2)
        
        if '7' in h_str or '7' in m_str:
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