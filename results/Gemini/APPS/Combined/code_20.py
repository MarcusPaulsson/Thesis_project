def solve():
    s = input()
    hh = int(s[:2])
    mm = int(s[3:])

    def is_palindrome(h, m):
        h_str = str(h).zfill(2)
        m_str = str(m).zfill(2)
        return h_str == m_str[::-1]

    minutes = 0
    while True:
        if is_palindrome(hh, mm):
            print(minutes)
            return

        mm += 1
        if mm == 60:
            mm = 0
            hh += 1
            if hh == 24:
                hh = 0
        minutes += 1

solve()