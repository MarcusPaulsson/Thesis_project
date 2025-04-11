def max_min_pieces(n, a, b):
    def can_distribute(x):
        plates_for_a = min(a // x, n)
        plates_for_b = min(b // x, n)
        return plates_for_a + plates_for_b >= n

    left, right = 1, max(a, b)
    answer = 0

    while left <= right:
        mid = (left + right) // 2
        if can_distribute(mid):
            answer = mid
            left = mid + 1
        else:
            right = mid - 1

    return answer

# Input reading
n, a, b = map(int, input().split())
print(max_min_pieces(n, a, b))