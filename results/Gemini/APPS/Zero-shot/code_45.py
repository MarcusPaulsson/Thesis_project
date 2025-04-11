def solve():
    n, k = map(int, input().split())

    if k * (k + 1) // 2 > n:
        print(-1)
        return

    best_gcd = 1
    for i in range(1, int(n**0.5) + 1):
        if n % i == 0:
            if n // i >= k * (k + 1) // 2:
                best_gcd = max(best_gcd, i)
            if i >= k * (k + 1) // 2:
                best_gcd = max(best_gcd, n // i)

    if best_gcd == 1 and k * (k + 1) // 2 > n:
        print(-1)
        return
    
    if best_gcd == 1 and n == 1 and k == 1:
        print(1)
        return

    if best_gcd == 1 and n == 1 and k > 1:
        print(-1)
        return

    
    first_k_sum = k * (k + 1) // 2
    remaining = n // best_gcd - first_k_sum
    
    if remaining < 0:
        print(-1)
        return

    result = []
    for i in range(1, k):
        result.append(i * best_gcd)
    result.append((k + remaining) * best_gcd)

    print(*result)

solve()