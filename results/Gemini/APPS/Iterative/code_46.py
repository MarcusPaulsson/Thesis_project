def solve():
    n, m = map(int, input().split())
    
    count = 0
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if (i + j) % 5 == 0:
                count += 1
    print(count)

def solve_optimized():
    n, m = map(int, input().split())
    
    count = 0
    for rem in range(5):
        count_n = (n - rem + 5) // 5 if rem <= n else 0
        count_m = (m - (5 - rem) % 5 + 5) // 5 if (5 - rem) % 5 <= m else 0
        count += count_n * count_m
    print(count)

def solve_optimized2():
    n, m = map(int, input().split())
    
    counts_n = [0] * 5
    counts_m = [0] * 5
    
    for i in range(1, n + 1):
        counts_n[i % 5] += 1
    for i in range(1, m + 1):
        counts_m[i % 5] += 1
        
    count = 0
    for i in range(5):
        count += counts_n[i] * counts_m[(5 - i) % 5]
    print(count)

solve_optimized2()