def max_min_pieces(n, a, b):
    left, right = 1, max(a, b)
    
    while left < right:
        mid = (left + right + 1) // 2
        if (a // mid) + (b // mid) >= n:
            left = mid
        else:
            right = mid - 1
            
    return left

# Read input
n, a, b = map(int, input().split())
# Get the result
result = max_min_pieces(n, a, b)
# Print the result
print(result)