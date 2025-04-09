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
        twos = 0
        threes = 0
        temp = m//n
        while temp % 2 == 0:
            temp //= 2
            twos += 1
        
        while temp % 3 == 0:
            temp //= 3
            threes += 1
        
        if temp != 1:
            print(-1)
        else:
            count_t = 0
            temp_t = m//n

            while temp_t > 1:
                if temp_t % 2 == 0:
                    temp_t //= 2
                    count_t += 1
                elif temp_t % 3 == 0:
                    temp_t //= 3
                    count_t += 1
                else:
                    count_t = -1
                    break

            print(count_t)

solve()