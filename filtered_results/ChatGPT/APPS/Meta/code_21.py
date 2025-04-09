def max_distance_after_swap(n, a):
    # Find positions of the minimum and maximum elements
    min_pos = a.index(1)
    max_pos = a.index(n)
    
    # Current distance
    current_distance = abs(min_pos - max_pos)

    # Calculate potential new distances by swapping min and max with ends
    potential_distances = [
        abs(0 - max_pos),  # Swap min (1) with the first element
        abs(n - 1 - max_pos),  # Swap min (1) with the last element
        abs(min_pos - 0),  # Swap max (n) with the first element
        abs(min_pos - (n - 1))  # Swap max (n) with the last element
    ]

    # Return the maximum possible distance after one swap
    return max(max(potential_distances), current_distance)

# Input reading
n = int(input())
a = list(map(int, input().split()))

# Output the result
print(max_distance_after_swap(n, a))