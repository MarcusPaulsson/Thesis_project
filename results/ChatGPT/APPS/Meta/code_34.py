def max_min_pieces(n, a, b):
    def can_distribute(x):
        plates_from_a = a // x
        plates_from_b = b // x
        return plates_from_a + plates_from_b >= n

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

n, a, b = map(int, input().split())
print(max_min_pieces(n, a, b))