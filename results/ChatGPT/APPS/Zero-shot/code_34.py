def max_min_pieces(n, a, b):
    left, right = 0, min(a, b) + 1
    
    while left < right:
        mid = (left + right + 1) // 2
        if (a // mid) + (b // mid) >= n:
            left = mid
        else:
            right = mid - 1
            
    return left

# Read input
n, a, b = map(int, input().split())
# Calculate and print the result
print(max_min_pieces(n, a, b))