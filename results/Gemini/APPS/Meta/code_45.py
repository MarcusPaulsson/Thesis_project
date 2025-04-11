def solve():
    n, k = map(int, input().split())

    if k * (k + 1) // 2 > n:
        print(-1)
        return

    best_gcd = 0
    for gcd in range(1, int(n**0.5) + 1):
        if n % gcd == 0:
            if n // gcd >= k * (k + 1) // 2:
                best_gcd = max(best_gcd, gcd)
            if gcd >= k * (k + 1) // 2:
                best_gcd = max(best_gcd, n // gcd)

    if best_gcd == 0:
        print(-1)
        return

    seq = [best_gcd * i for i in range(1, k)]
    remaining = n - sum(seq)
    seq.append(remaining)

    if all(seq[i] < seq[i+1] for i in range(len(seq)-1)) and all(x > 0 for x in seq):
        print(*seq)
    else:
        print(-1)

solve()