def max_subarray_sum(arr):
    max_sum = 0
    current_sum = 0
    for num in arr:
        current_sum = max(num, current_sum + num)
        max_sum = max(max_sum, current_sum)
    return max_sum

def max_beauty_with_multiplication(n, x, a):
    original_beauty = max_subarray_sum(a)
    
    if x == 1:
        return original_beauty
    
    # Calculate prefix sums
    prefix_sum = [0] * (n + 1)
    for i in range(n):
        prefix_sum[i + 1] = prefix_sum[i] + a[i]

    max_gain = 0
    
    # We will consider every possible subarray [l, r]
    for l in range(n):
        for r in range(l, n):
            # Subarray a[l:r+1] will be multiplied by x
            subarray_sum = prefix_sum[r + 1] - prefix_sum[l]
            new_subarray_sum = subarray_sum * x
            # Gain from changing this subarray
            gain = new_subarray_sum - subarray_sum
            
            # Update maximum gain
            max_gain = max(max_gain, gain)

    return original_beauty + max_gain

# Read input
n, x = map(int, input().split())
a = list(map(int, input().split()))

# Calculate and print the result
result = max_beauty_with_multiplication(n, x, a)
print(result)