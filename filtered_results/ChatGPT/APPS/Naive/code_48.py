def kth_largest_in_multiplication_table(n, m, k):
    def count_less_equal(x):
        count = 0
        for i in range(1, n + 1):
            count += min(x // i, m)
        return count

    left, right = 1, n * m
    while left < right:
        mid = (left + right) // 2
        if count_less_equal(mid) < k:
            left = mid + 1
        else:
            right = mid
    return left

# Input reading
n, m, k = map(int, input().split())
# Output the result
print(kth_largest_in_multiplication_table(n, m, k))