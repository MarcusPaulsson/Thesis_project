def max_min_pieces(n, a, b):
    def can_distribute(x):
        plates_for_a = (a + x - 1) // x  # ceil(a / x)
        plates_for_b = (b + x - 1) // x  # ceil(b / x)
        return plates_for_a + plates_for_b <= n

    low, high = 1, max(a, b)
    result = 0

    while low <= high:
        mid = (low + high) // 2
        if can_distribute(mid):
            result = mid
            low = mid + 1
        else:
            high = mid - 1

    return result

# Input reading
n, a, b = map(int, input().split())
print(max_min_pieces(n, a, b))