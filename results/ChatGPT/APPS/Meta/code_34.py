def max_min_pieces(n, a, b):
    def can_distribute(x):
        plates_for_a = min(n, a // x)
        plates_for_b = min(n - plates_for_a, b // x)
        return plates_for_a + plates_for_b >= n

    left, right = 1, max(a, b)
    result = 0

    while left <= right:
        mid = (left + right) // 2
        if can_distribute(mid):
            result = mid
            left = mid + 1
        else:
            right = mid - 1

    return result

# Read input
n, a, b = map(int, input().split())
# Calculate and print the result
print(max_min_pieces(n, a, b))