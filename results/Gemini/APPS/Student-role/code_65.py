def solve():
    n, m = map(int, input().split())

    if n == m:
        print(0)
        return

    if m % n != 0:
        print(-1)
        return

    q = m // n
    
    count = 0
    while q % 2 == 0:
        q //= 2
        count += 1
    while q % 3 == 0:
        q //= 3
        count += 1
    
    if q != 1:
        print(-1)
    else:
        print(count)

solve()