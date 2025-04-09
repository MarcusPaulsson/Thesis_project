def max_distance_after_swap(n, a):
    min_index = a.index(1)
    max_index = a.index(n)

    # Calculate current distance
    current_distance = abs(min_index - max_index)

    # Possible new positions for min (1) and max (n) after swap
    new_positions = [
        (0, max_index),        # Swap with first element
        (n - 1, max_index),    # Swap with last element
        (min_index, 0),        # Swap with first element
        (min_index, n - 1)     # Swap with last element
    ]

    max_distance = current_distance

    for new_pos in new_positions:
        new_min_index, new_max_index = new_pos
        if a[new_min_index] == 1 or a[new_max_index] == n:
            distance = abs(new_min_index - new_max_index)
            max_distance = max(max_distance, distance)

    return max_distance

# Input reading
n = int(input())
a = list(map(int, input().split()))

# Output the result
print(max_distance_after_swap(n, a))