def solve():
    n, k = map(int, input().split())

    if k * (k + 1) // 2 > n:
        print(-1)
        return

    best_gcd = 0
    for gcd in range(int(n**0.5), 0, -1):
        if n % gcd == 0:
            if n // gcd >= k * (k + 1) // 2:
                best_gcd = gcd
                break
            if gcd >= k * (k + 1) // 2:
                best_gcd = n // gcd
                break

    if best_gcd == 0:
        print(-1)
        return

    result = []
    sum_so_far = 0
    for i in range(1, k):
        result.append(best_gcd * i)
        sum_so_far += best_gcd * i

    result.append(n - sum_so_far)

    if result[-1] <= result[-2]:
        print(-1)
        return

    print(*result)

solve()