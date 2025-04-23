def solve():
    n, m = map(int, input().split())

    if n == m:
        print(0)
        return

    if m % n != 0:
        print(-1)
        return

    k = m // n
    
    count = 0
    twos = 0
    threes = 0
    
    while k % 2 == 0:
        k //= 2
        twos += 1
    while k % 3 == 0:
        k //= 3
        threes += 1
    
    if k == 1:
        print(twos + threes)
    else:
        print(-1)

solve()