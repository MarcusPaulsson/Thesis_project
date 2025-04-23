def solve():
    n, k = map(int, input().split())
    
    if k * (k + 1) // 2 > n:
        print(-1)
        return
    
    if k == 1:
        print(n)
        return
    
    if n % k != 0:
        print(-1)
        return
    
    base = n // k
    
    if base <= 0:
        print(-1)
        return
    
    result = [base + i for i in range(k)]
    
    total_sum = sum(result)
    
    if total_sum == n:
        print(*result)
        return
    
    diff = n - total_sum
    
    for i in range(k - 1, -1, -1):
        add = min(diff, k - i - 1)
        result[i] += add
        diff -= add
        if diff == 0:
            break
    
    if diff != 0:
        print(-1)
        return
    
    print(*result)