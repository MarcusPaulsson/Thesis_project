def solve():
    n, m = map(int, input().split())

    if n == m:
        print(0)
        return

    if m % n != 0:
        print(-1)
        return

    diff = m // n
    
    twos = 0
    threes = 0
    
    while diff % 2 == 0:
        diff //= 2
        twos += 1
    while diff % 3 == 0:
        diff //= 3
        threes += 1
            
    if diff != 1:
        print(-1)
    else:
        print(twos + threes)

solve()