def max_distance_after_swap(n, a):
    min_index = a.index(1)
    max_index = a.index(n)

    # Calculate initial distance
    initial_distance = abs(min_index - max_index)

    # Possible new positions after swap
    new_positions = [
        (0, max_index),  # Swap 1 with the first element
        (n - 1, max_index),  # Swap 1 with the last element
        (min_index, 0),  # Swap n with the first element
        (min_index, n - 1)  # Swap n with the last element
    ]

    # Calculate maximum distance after one swap
    max_distance = initial_distance
    for new_pos in new_positions:
        new_distance = abs(new_pos[0] - new_pos[1])
        max_distance = max(max_distance, new_distance)

    return max_distance

# Read input
n = int(input())
a = list(map(int, input().split()))

# Get the result and print it
result = max_distance_after_swap(n, a)
print(result)