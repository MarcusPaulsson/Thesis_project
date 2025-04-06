def kth_largest_in_multiplication_table(n, m, k):
    left, right = 1, n * m
    
    while left < right:
        mid = (left + right) // 2
        count = 0
        
        for i in range(1, n + 1):
            count += min(mid // i, m)
        
        if count < k:
            left = mid + 1
        else:
            right = mid
            
    return left

# Read input
n, m, k = map(int, input().split())
# Output the k-th largest number
print(kth_largest_in_multiplication_table(n, m, k))