def solve():
    s = input()
    hh = int(s[:2])
    mm = int(s[3:])

    ans = 0
    while True:
        hh_str = str(hh).zfill(2)
        mm_str = str(mm).zfill(2)
        
        if hh_str == mm_str[::-1]:
            print(ans)
            return

        mm += 1
        if mm == 60:
            mm = 0
            hh += 1
            if hh == 24:
                hh = 0
        ans += 1

solve()