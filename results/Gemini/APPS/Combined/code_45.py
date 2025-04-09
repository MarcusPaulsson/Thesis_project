def solve():
    n, k = map(int, input().split())

    if k * (k + 1) // 2 > n:
        print(-1)
        return

    best_gcd = -1
    best_seq = []

    for gcd in range(int(n**0.5), 0, -1):
        if n % gcd == 0:
            divisors = [gcd, n // gcd]
            for d in divisors:
                if (n // d) >= k * (k + 1) // 2:
                    remaining = (n // d) - k * (k + 1) // 2
                    seq = [i + 1 for i in range(k)]
                    
                    base_addition = remaining // k
                    remainder_addition = remaining % k

                    for i in range(k):
                        seq[i] += base_addition
                    
                    for i in range(k - 1, k - 1 - remainder_addition, -1):
                        seq[i] += 1
                    
                    seq = [x * d for x in seq]
                    
                    is_strictly_increasing = all(seq[i] < seq[i+1] for i in range(len(seq)-1))
                    if is_strictly_increasing:
                        print(*seq)
                        return

    print(-1)

solve()