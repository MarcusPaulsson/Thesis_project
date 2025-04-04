def kth_largest_number(n, m, k):
    if n > m:
        n, m = m, n
    low, high = 1, n * m
    while low < high:
        mid = (low + high) // 2
        count = 0
        for i in range(1, n + 1):
            count += min(mid // i, m)
        if count < k:
            low = mid + 1
        else:
            high = mid
    return low

n, m, k = map(int, input().split())
print(kth_largest_number(n, m, k))