def solve():
    n, m = map(int, input().split())

    if n == m:
        print(0)
        return

    if m % n != 0:
        print(-1)
        return

    div = m // n
    
    count = 0
    while div % 2 == 0:
        div //= 2
        count += 1
    while div % 3 == 0:
        div //= 3
        count += 1
    
    if div == 1:
        print(count)
    else:
        print(-1)

solve()