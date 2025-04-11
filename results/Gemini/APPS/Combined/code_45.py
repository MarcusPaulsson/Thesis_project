def solve():
    n, k = map(int, input().split())

    if k * (k + 1) // 2 > n:
        print(-1)
        return

    best_gcd = 0
    for gcd in range(1, int(n**0.5) + 1):
        if n % gcd == 0:
            if (n // gcd) >= (k * (k + 1) // 2):
                best_gcd = max(best_gcd, gcd)
            if gcd >= (k * (k + 1) // 2):
                best_gcd = max(best_gcd, n // gcd)

    if best_gcd == 0:
        print(-1)
        return
    
    seq = []
    sum_so_far = 0
    for i in range(1, k):
        seq.append(best_gcd * i)
        sum_so_far += best_gcd * i

    seq.append(n - sum_so_far)

    if seq[-1] <= seq[-2]:
        print(-1)
        return

    print(*seq)

solve()