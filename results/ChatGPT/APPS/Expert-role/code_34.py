def can_distribute(x, n, a, b):
    # Calculate how many plates can be filled with at least x pieces
    plates_from_a = a // x
    plates_from_b = b // x
    # Check if we can fill at least n plates with the pieces
    return plates_from_a + plates_from_b >= n

def maximum_minimum_pieces(n, a, b):
    left, right = 1, max(a, b)  # x should be at least 1 and at most max(a, b)
    answer = 0

    while left <= right:
        mid = (left + right) // 2
        if can_distribute(mid, n, a, b):
            answer = mid  # mid is a possible solution
            left = mid + 1  # try for a bigger x
        else:
            right = mid - 1  # try for a smaller x

    return answer

# Read input
n, a, b = map(int, input().split())
# Get the result and print it
print(maximum_minimum_pieces(n, a, b))