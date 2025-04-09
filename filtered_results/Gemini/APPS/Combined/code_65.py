def solve():
    n, m = map(int, input().split())

    if n == m:
        print(0)
        return

    if m % n != 0:
        print(-1)
        return

    diff = m // n
    
    two_count = 0
    three_count = 0
    
    while diff % 2 == 0:
        diff //= 2
        two_count += 1
    while diff % 3 == 0:
        diff //= 3
        three_count += 1
        
    if diff != 1:
        print(-1)
    else:
        print(two_count + three_count)

solve()