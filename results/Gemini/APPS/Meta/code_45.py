def solve():
    n, k = map(int, input().split())

    if k * (k + 1) // 2 > n:
        print(-1)
        return

    best_gcd = 0
    best_seq = []

    for gcd in range(int(n**0.5), 0, -1):
        if n % gcd == 0:
            q = n // gcd
            if q >= k * (k + 1) // 2:
                remaining = q - k * (k + 1) // 2
                seq = [i + 1 for i in range(k)]
                seq[-1] += remaining
                seq = [x * gcd for x in seq]
                
                print(*seq)
                return
            
            gcd2 = n // gcd
            q = n // gcd2
            if q >= k * (k + 1) // 2:
                remaining = q - k * (k + 1) // 2
                seq = [i + 1 for i in range(k)]
                seq[-1] += remaining
                seq = [x * gcd2 for x in seq]
                
                print(*seq)
                return

    print(-1)

solve()