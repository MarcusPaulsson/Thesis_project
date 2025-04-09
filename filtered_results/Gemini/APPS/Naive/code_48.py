def solve():
    n, m, k = map(int, input().split())

    def count_less_equal(x):
        count = 0
        for i in range(1, n + 1):
            count += min(m, x // i)
        return count

    left = 1
    right = n * m
    ans = 0

    while left <= right:
        mid = (left + right) // 2
        if count_less_equal(mid) >= k:
            ans = mid
            right = mid - 1
        else:
            left = mid + 1

    print(ans)

solve()