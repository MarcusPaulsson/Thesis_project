def max_min_pieces(n, a, b):
    low, high = 1, max(a, b)

    while low < high:
        mid = (low + high + 1) // 2
        # Check if we can satisfy the condition with mid as the minimum pieces
        if (a // mid) + (b // mid) >= n:
            low = mid
        else:
            high = mid - 1

    return low

# Read input
n, a, b = map(int, input().split())
# Get the result and print
print(max_min_pieces(n, a, b))