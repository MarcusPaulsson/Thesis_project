def solve():
    n, m = map(int, input().split())

    if n == m:
        print(0)
        return

    if m % n != 0:
        print(-1)
        return

    diff = m // n
    
    count = 0
    while diff % 2 == 0:
        diff //= 2
        count += 1
    while diff % 3 == 0:
        diff //= 3
        count += 1
    
    if diff != 1:
        print(-1)
    else:
        
        num_twos = 0
        num_threes = 0
        
        temp = m // n
        while temp % 2 == 0:
            temp //= 2
            num_twos += 1
        while temp % 3 == 0:
            temp //= 3
            num_threes += 1
        
        if temp != 1:
            print(-1)
        else:
            print(num_twos + num_threes)

solve()