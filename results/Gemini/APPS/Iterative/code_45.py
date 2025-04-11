def solve():
    n, k = map(int, input().split())

    if k * (k + 1) // 2 > n:
        print(-1)
        return

    best_gcd = 0
    for i in range(1, int(n**0.5) + 1):
        if n % i == 0:
            if n // i >= k * (k + 1) // 2:
                best_gcd = max(best_gcd, i)
            if i >= k * (k + 1) // 2:
                best_gcd = max(best_gcd, n // i)

    if best_gcd == 0:
        print(-1)
        return

    first = best_gcd
    result = []
    for i in range(1, k):
        result.append(first * i)
    result.append(n - sum(result))

    if result[-1] <= result[-2] or any(x <= 0 for x in result):
        print(-1)
    else:
        print(*result)

solve()