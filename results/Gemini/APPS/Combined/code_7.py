def solve():
    n, m = map(int, input().split())

    left = 0
    right = 2 * 10**9  # Adjusted upper bound

    ans = right

    while left <= right:
        mid = (left + right) // 2

        total_sparrows = mid * (mid + 1) // 2
        
        barn_content = n + mid * m
        
        if barn_content >= total_sparrows:
            ans = mid
            right = mid - 1
        else:
            left = mid + 1

    print(ans)

solve()