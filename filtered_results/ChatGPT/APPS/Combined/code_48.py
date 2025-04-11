def kth_largest_in_multiplication_table(n, m, k):
    left, right = 1, n * m
    
    while left < right:
        mid = (left + right) // 2
        count = sum(min(mid // i, m) for i in range(1, n + 1))
        
        if count < k:
            left = mid + 1
        else:
            right = mid
            
    return left

# Input reading
n, m, k = map(int, input().split())
print(kth_largest_in_multiplication_table(n, m, k))