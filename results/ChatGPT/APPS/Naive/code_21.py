def max_distance_after_swap(n, a):
    min_index = a.index(1)
    max_index = a.index(n)

    # Calculate current distance
    current_distance = abs(min_index - max_index)

    # Possible new positions after swap
    new_positions = [
        (0, max_index),  # Swap min with first element
        (n - 1, max_index),  # Swap min with last element
        (min_index, 0),  # Swap max with first element
        (min_index, n - 1)  # Swap max with last element
    ]

    max_distance = current_distance

    for new_pos in new_positions:
        new_min_index, new_max_index = new_pos
        max_distance = max(max_distance, abs(new_min_index - new_max_index))

    return max_distance

# Input reading
n = int(input())
a = list(map(int, input().split()))

# Output the result
print(max_distance_after_swap(n, a))