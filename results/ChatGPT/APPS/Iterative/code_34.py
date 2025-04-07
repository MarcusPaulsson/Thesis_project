def can_distribute(x, n, a, b):
    plates_for_a = (a + x - 1) // x  # Ceiling division of a by x
    plates_for_b = (b + x - 1) // x  # Ceiling division of b by x
    return plates_for_a + plates_for_b <= n

def max_min_pieces(n, a, b):
    low, high = 1, max(a, b)
    while low < high:
        mid = (low + high + 1) // 2
        if can_distribute(mid, n, a, b):
            low = mid  # mid is a valid distribution, try for a larger minimum
        else:
            high = mid - 1  # mid is too large, try a smaller minimum
    return low

n, a, b = map(int, input().split())
print(max_min_pieces(n, a, b))