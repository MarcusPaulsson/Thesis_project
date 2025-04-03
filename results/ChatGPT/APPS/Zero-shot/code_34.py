def max_min_pieces(n, a, b):
    def can_distribute(x):
        plates_from_a = a // x
        plates_from_b = b // x
        return plates_from_a + plates_from_b >= n
    
    low, high = 1, max(a, b)
    result = 0
    
    while low <= high:
        mid = (low + high) // 2
        if can_distribute(mid):
            result = mid
            low = mid + 1
        else:
            high = mid - 1
    
    return result

# Read input
n, a, b = map(int, input().split())

# Compute and print the result
print(max_min_pieces(n, a, b))