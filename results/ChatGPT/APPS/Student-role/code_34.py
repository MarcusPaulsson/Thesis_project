def can_distribute(x, n, a, b):
    # Calculate how many plates can be filled with at least x pieces
    plates_from_a = a // x
    plates_from_b = b // x
    # Check if the total plates filled can satisfy n
    return plates_from_a + plates_from_b >= n

def max_min_pieces(n, a, b):
    low, high = 1, max(a, b)
    result = 0
    while low <= high:
        mid = (low + high) // 2
        if can_distribute(mid, n, a, b):
            result = mid  # mid is a potential solution
            low = mid + 1  # Try for a larger value
        else:
            high = mid - 1  # Try for a smaller value
    return result

# Input
n, a, b = map(int, input().split())
# Output
print(max_min_pieces(n, a, b))