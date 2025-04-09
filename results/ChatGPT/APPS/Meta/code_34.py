def max_min_pieces(n, a, b):
    # Binary search to find the maximum possible x
    left, right = 1, max(a, b)
    answer = 0
    
    while left <= right:
        mid = (left + right) // 2
        
        # Check if we can distribute pieces with at least mid pieces per plate
        plates_for_a = a // mid
        plates_for_b = b // mid
        
        # We need at least n plates in total
        if plates_for_a + plates_for_b >= n:
            answer = mid  # We can achieve at least mid pieces per plate
            left = mid + 1  # Try for a larger value
        else:
            right = mid - 1  # Try for a smaller value
    
    return answer

# Input reading
n, a, b = map(int, input().split())
# Output the result
print(max_min_pieces(n, a, b))