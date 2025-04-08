def maximum_distance_after_swap(n, a):
    # Find the indices of the minimum and maximum elements
    min_index = a.index(1)
    max_index = a.index(n)

    # Calculate the current distance
    current_distance = abs(min_index - max_index)

    # Potential maximum distances after one swap
    distance_with_first = abs(0 - max_index)  # Swap 1 with a[0]
    distance_with_last = abs(n - 1 - max_index)  # Swap 1 with a[n-1]
    distance_with_first_min = abs(min_index - 0)  # Swap n with a[0]
    distance_with_last_min = abs(min_index - (n - 1))  # Swap n with a[n-1]

    # Calculate the maximum possible distance
    max_distance = max(current_distance, distance_with_first, distance_with_last,
                       distance_with_first_min, distance_with_last_min)

    return max_distance

# Reading input
n = int(input().strip())
a = list(map(int, input().strip().split()))

# Output the result
print(maximum_distance_after_swap(n, a))