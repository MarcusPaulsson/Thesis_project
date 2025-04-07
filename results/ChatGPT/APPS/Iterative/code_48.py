def kth_largest_in_multiplication_table(n, m, k):
    # Binary search to find the k-th largest number
    left, right = 1, n * m
    
    while left < right:
        mid = (left + right) // 2
        
        # Count how many numbers are less than or equal to mid
        count = 0
        for i in range(1, n + 1):
            count += min(mid // i, m)
        
        # If count is less than k, we need a larger number
        if count < k:
            left = mid + 1
        else:
            right = mid
    
    return left

# Read input
n, m, k = map(int, input().split())
# Get the k-th largest number
result = kth_largest_in_multiplication_table(n, m, k)
# Print the result
print(result)