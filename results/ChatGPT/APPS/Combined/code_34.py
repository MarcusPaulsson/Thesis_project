def max_min_pieces(n, a, b):
    low, high = 1, max(a, b)
    result = 0
    
    while low <= high:
        mid = (low + high) // 2
        
        # Calculate the number of plates we can fill with at least mid pieces of each cake
        plates_from_a = a // mid
        plates_from_b = b // mid
        
        # Total plates filled must be at least n
        if plates_from_a + plates_from_b >= n:
            result = mid  # mid is a valid solution
            low = mid + 1  # try for a bigger x
        else:
            high = mid - 1  # try for a smaller x
            
    return result

# Read input
n, a, b = map(int, input().split())
# Output the result
print(max_min_pieces(n, a, b))