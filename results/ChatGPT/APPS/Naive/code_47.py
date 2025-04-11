def max_subarray_sum(arr):
    max_sum = 0
    current_sum = 0
    for num in arr:
        current_sum += num
        if current_sum < 0:
            current_sum = 0
        max_sum = max(max_sum, current_sum)
    return max_sum

def max_beauty_with_multiplier(n, x, a):
    # Calculate the original beauty of the array
    original_beauty = max_subarray_sum(a)
    
    # If x is 0, the best we can do is the original beauty
    if x == 0:
        return original_beauty
    
    # Calculate the maximum beauty after applying the multiplier
    max_beauty = original_beauty
    for i in range(n):
        # We will consider subarrays starting from index i
        current_sum = 0
        for j in range(i, n):
            current_sum += a[j]
            # Calculate the beauty if we multiply the subarray a[i:j+1] by x
            modified_sum = current_sum * x
            # Calculate the beauty of the remaining parts
            left_sum = max_subarray_sum(a[:i])
            right_sum = max_subarray_sum(a[j+1:])
            total_beauty = left_sum + modified_sum + right_sum
            max_beauty = max(max_beauty, total_beauty)
    
    return max_beauty

# Input reading
n, x = map(int, input().split())
a = list(map(int, input().split()))

# Output the result
print(max_beauty_with_multiplier(n, x, a))