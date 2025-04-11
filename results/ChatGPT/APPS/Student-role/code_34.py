def max_min_pieces(n, a, b):
    def can_distribute(x):
        plates_for_a = (a + x - 1) // x  # Ceiling division
        plates_for_b = (b + x - 1) // x  # Ceiling division
        return plates_for_a + plates_for_b <= n

    left, right = 1, max(a, b)
    while left < right:
        mid = (left + right + 1) // 2
        if can_distribute(mid):
            left = mid
        else:
            right = mid - 1
    return left

n, a, b = map(int, input().split())
print(max_min_pieces(n, a, b))