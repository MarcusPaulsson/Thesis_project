def max_distance_after_swap(n, a):
    min_index = a.index(1)
    max_index = a.index(n)
    
    # Calculate the current distance
    current_distance = abs(min_index - max_index)
    
    # Calculate potential distances after swaps
    distance1 = abs(min_index - (n - 1))  # swap min with last element
    distance2 = abs(max_index - 0)        # swap max with first element
    distance3 = abs(max_index - (n - 1))  # swap max with last element
    distance4 = abs(min_index - 0)        # swap min with first element
    
    # The maximum distance possible after one swap
    max_distance = max(current_distance, distance1, distance2, distance3, distance4)
    
    return max_distance

# Input reading
n = int(input())
a = list(map(int, input().split()))

# Output the result
print(max_distance_after_swap(n, a))