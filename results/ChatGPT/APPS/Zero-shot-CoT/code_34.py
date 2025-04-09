def max_min_pieces(n, a, b):
    def can_distribute(x):
        plates_cake1 = a // x
        plates_cake2 = b // x
        return plates_cake1 + plates_cake2 >= n

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