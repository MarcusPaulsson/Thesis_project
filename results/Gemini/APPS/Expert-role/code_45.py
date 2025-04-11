def solve():
    n, k = map(int, input().split())

    if k * (k + 1) // 2 > n:
        print("-1")
        return

    best_gcd = 1
    for i in range(1, int(n**0.5) + 1):
        if n % i == 0:
            if n // i >= k * (k + 1) // 2:
                best_gcd = max(best_gcd, i)
            if i >= k * (k + 1) // 2:
                best_gcd = max(best_gcd, n // i)

    first = best_gcd
    remaining_sum = n // best_gcd
    
    if k * (k + 1) // 2 > remaining_sum:
        print("-1")
        return

    result = []
    for i in range(1, k):
        result.append(first * i)
        remaining_sum -= i

    result.append(first * remaining_sum)

    for x in result:
        print(x, end=" ")
    print()

solve()