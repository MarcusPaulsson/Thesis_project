def solve():
    n, m = map(int, input().split())
    
    count = 0
    for remainder in range(5):
        count += (n - remainder + 4) // 5 * ((m - (5 - remainder) + 5) // 5) if remainder <= n else 0
    print(count)

solve()