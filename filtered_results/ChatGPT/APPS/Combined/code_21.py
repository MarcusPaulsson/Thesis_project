def max_distance_after_swap(n, a):
    min_index = a.index(1)
    max_index = a.index(n)

    # Current distance
    current_distance = abs(min_index - max_index)

    # Calculate potential new distances after swapping
    potential_distances = [
        abs(0 - max_index),  # Swap 1 with the first element
        abs(n - 1 - max_index),  # Swap 1 with the last element
        abs(min_index - 0),  # Swap n with the first element
        abs(min_index - (n - 1))  # Swap n with the last element
    ]

    # The maximum distance after one swap
    max_distance = max(current_distance, *potential_distances)

    return max_distance

# Input reading
n = int(input())
a = list(map(int, input().split()))

# Output the result
print(max_distance_after_swap(n, a))