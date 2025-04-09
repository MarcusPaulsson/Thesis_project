def max_subarray_sum(arr):
    max_ending_here = max_so_far = 0
    for x in arr:
        max_ending_here = max(0, max_ending_here + x)
        max_so_far = max(max_so_far, max_ending_here)
    return max_so_far

def max_beauty_with_operation(n, x, a):
    # Calculate the beauty of the original array
    original_beauty = max_subarray_sum(a)

    # Calculate the beauty after multiplying a subarray by x
    max_gain = 0
    current_sum = 0
    for i in range(n):
        current_sum += a[i]
        # Calculate the gain if we multiply the current prefix and the suffix
        if i > 0:
            max_gain = max(max_gain, current_sum * x - max_subarray_sum(a[:i]))
        if i < n - 1:
            max_gain = max(max_gain, current_sum * x - max_subarray_sum(a[i + 1:]))
        
        # Reset current sum if it goes negative
        if current_sum < 0:
            current_sum = 0

    # Calculate the maximum possible beauty
    return max(original_beauty, original_beauty + max_gain)

# Read input
n, x = map(int, input().split())
a = list(map(int, input().split()))

# Calculate and print the maximum beauty
print(max_beauty_with_operation(n, x, a))