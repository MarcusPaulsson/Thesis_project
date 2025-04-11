def solve():
    n, k = map(int, input().split())

    if k * (k + 1) // 2 > n:
        print("-1")
        return

    best_gcd = 0
    best_seq = []

    for gcd in range(int(n**0.5), 0, -1):
        if n % gcd == 0:
            q = n // gcd
            if q >= k * (k + 1) // 2:
                
                seq = [gcd * i for i in range(1, k)]
                last = n - sum(seq)
                if last > seq[-1]:
                   
                    best_gcd = gcd
                    best_seq = seq + [last]
                    break
            q = gcd
            gcd = n // gcd
            if q >= k * (k + 1) // 2:
                
                seq = [gcd * i for i in range(1, k)]
                last = n - sum(seq)
                if last > seq[-1]:
                    
                    best_gcd = gcd
                    best_seq = seq + [last]
                    break

    if best_gcd == 0:
        if n == 1 and k == 1:
            print(1)
        else:
            print("-1")
    else:
        print(*best_seq)

solve()