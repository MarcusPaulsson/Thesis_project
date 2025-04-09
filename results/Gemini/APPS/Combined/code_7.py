def solve():
    n, m = map(int, input().split())

    left = 0
    right = 2 * 10**9  #Refined range for binary search

    ans = right

    while left <= right:
        mid = (left + right) // 2
        
        total_sparrows = mid * (mid + 1) // 2
        
        grain_after_sparrows = n + mid * m - total_sparrows

        if grain_after_sparrows <= 0:
            ans = mid
            right = mid - 1
        else:
            left = mid + 1

    print(ans)

solve()