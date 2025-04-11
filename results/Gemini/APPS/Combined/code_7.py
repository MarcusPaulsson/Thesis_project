def solve():
    n, m = map(int, input().split())

    low = 0
    high = 2 * 10**9  # Increased the upper bound for binary search
    ans = -1

    while low <= high:
        mid = (low + high) // 2
        
        total_sparrows = mid * (mid + 1) // 2
        
        barn_content = n + mid * m - total_sparrows
        
        if barn_content <= 0:
            ans = mid
            high = mid - 1
        else:
            low = mid + 1

    print(ans)

solve()