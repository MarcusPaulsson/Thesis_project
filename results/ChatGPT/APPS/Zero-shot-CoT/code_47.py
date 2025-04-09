def max_subarray_sum(arr):
    max_ending_here = max_so_far = 0
    for x in arr:
        max_ending_here = max(0, max_ending_here + x)
        max_so_far = max(max_so_far, max_ending_here)
    return max_so_far

def max_beauty_after_operation(n, x, a):
    # Calculate the original beauty of the array
    original_beauty = max_subarray_sum(a)

    # If x is 1 or 0, multiplying won't increase the beauty
    if x >= 1:
        return original_beauty

    # We will calculate the maximum beauty after multiplying a subarray
    max_increase = 0

    # Calculate the maximum sum we can get by considering the effect of multiplying a subarray by x
    current_sum = 0
    for i in range(n):
        current_sum += a[i]
        # When we multiply a subarray, the contribution changes, we consider the effect of multiplying up to the current index
        # We find the maximum sum of the array with the impact of multiplying by x
        max_increase = max(max_increase, current_sum * x)
        # Reset the current_sum if it goes negative
        if current_sum < 0:
            current_sum = 0

    # The new beauty will be the original beauty plus the maximum increase we can get from the operation
    return max(original_beauty, original_beauty + max_increase)

# Input reading
n, x = map(int, input().split())
a = list(map(int, input().split()))

# Calculate and print the result
print(max_beauty_after_operation(n, x, a))