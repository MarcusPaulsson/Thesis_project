def solve():
    time_str = input()
    hh = int(time_str[:2])
    mm = int(time_str[3:])

    def is_palindrome(h, m):
        h_str = str(h).zfill(2)
        m_str = str(m).zfill(2)
        return h_str == m_str[::-1]

    minutes = 0
    while True:
        if is_palindrome(hh, mm):
            print(minutes)
            return

        minutes += 1
        mm += 1
        if mm == 60:
            mm = 0
            hh += 1
            if hh == 24:
                hh = 0

solve()