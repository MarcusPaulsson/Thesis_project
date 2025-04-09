def solve():
    x = int(input())
    hh, mm = map(int, input().split())

    def is_lucky(h, m):
        return '7' in str(h) or '7' in str(m)
    
    count = 0
    h = hh
    m = mm
    
    while True:
        if is_lucky(h, m):
            print(count)
            return
        
        m -= x
        if m < 0:
            m += 60
            h -= 1
            if h < 0:
                h += 24
        
        count += 1

solve()