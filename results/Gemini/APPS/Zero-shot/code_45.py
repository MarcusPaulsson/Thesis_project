def solve():
    n, k = map(int, input().split())

    def find_gcd(n, k):
        best_gcd = -1
        for i in range(1, int(n**0.5) + 1):
            if n % i == 0:
                if n // i >= k * (k + 1) // 2:
                    best_gcd = max(best_gcd, i)
                if i >= k * (k + 1) // 2:
                    best_gcd = max(best_gcd, n // i)
        return best_gcd
    
    gcd = find_gcd(n, k)
    
    if gcd == -1:
        print(-1)
        return
    
    result = []
    for i in range(1, k):
        result.append(i * gcd)
    
    result.append(n - sum(result))
    
    if result[-1] <= result[-2]:
        print(-1)
        return
        
    print(*result)

solve()