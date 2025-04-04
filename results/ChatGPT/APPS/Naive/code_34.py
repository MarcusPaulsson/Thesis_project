def max_min_pieces(n, a, b):
    def can_distribute(x):
        plates_for_first_cake = (a + x - 1) // x  # ceiling division
        plates_for_second_cake = (b + x - 1) // x  # ceiling division
        return plates_for_first_cake + plates_for_second_cake <= n

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

# Input
n, a, b = map(int, input().split())
# Output
print(max_min_pieces(n, a, b))