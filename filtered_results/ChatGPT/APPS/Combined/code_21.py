def max_distance_after_swap(n, a):
    # Find the positions of the minimum (1) and maximum (n) elements
    min_index = a.index(1)
    max_index = a.index(n)
    
    # Calculate the current distance
    current_distance = abs(min_index - max_index)
    
    # Calculate potential new distances by swapping min and max with ends of the array
    distance_min_to_left = abs(0 - max_index)  # Swap min (1) with the leftmost element
    distance_min_to_right = abs(n - 1 - max_index)  # Swap min (1) with the rightmost element
    distance_max_to_left = abs(0 - min_index)  # Swap max (n) with the leftmost element
    distance_max_to_right = abs(n - 1 - min_index)  # Swap max (n) with the rightmost element
    
    # Calculate the maximum possible distance
    max_distance = max(current_distance, distance_min_to_left, distance_min_to_right,
                       distance_max_to_left, distance_max_to_right)
    
    return max_distance

# Input handling
n = int(input())
a = list(map(int, input().split()))

# Output the result
print(max_distance_after_swap(n, a))