def solve():
    n, m, k = map(int, input().split())

    def count_less_equal(x):
        count = 0
        for i in range(1, n + 1):
            count += min(m, x // i)
        return count

    low = 1
    high = n * m
    ans = 0
    while low <= high:
        mid = (low + high) // 2
        if count_less_equal(mid) >= k:
            ans = mid
            high = mid - 1
        else:
            low = mid + 1
    print(ans)

solve()