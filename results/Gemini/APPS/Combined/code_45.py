def solve():
    n, k = map(int, input().split())

    if k * (k + 1) // 2 > n:
        print("-1")
        return

    best_gcd = 0
    best_seq = []

    for gcd in range(int(n**0.5), 0, -1):
        if n % gcd == 0:
            divisors = [gcd, n // gcd]
            for d in divisors:
                if d >= k * (k + 1) // 2:
                    remaining_sum = d - k * (k + 1) // 2
                    seq = [i + 1 for i in range(k)]
                    seq[-1] += remaining_sum
                    seq = [x * (n // d) for x in seq]

                    is_strictly_increasing = all(seq[i] < seq[i+1] for i in range(len(seq)-1))
                    if is_strictly_increasing:
                        best_gcd = n // d
                        best_seq = seq
                        print(*best_seq)
                        return

    if n == 1 and k == 1:
        print(1)
    else:
        print("-1")

solve()