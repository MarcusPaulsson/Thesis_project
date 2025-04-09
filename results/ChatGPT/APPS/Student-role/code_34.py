def max_min_pieces(n, a, b):
    left, right = 1, max(a, b)
    
    while left < right:
        mid = (left + right + 1) // 2
        plates_for_a = (a + mid - 1) // mid
        plates_for_b = (b + mid - 1) // mid
        
        if plates_for_a + plates_for_b <= n:
            left = mid
        else:
            right = mid - 1
            
    return left

# Input
n, a, b = map(int, input().split())
# Output
print(max_min_pieces(n, a, b))