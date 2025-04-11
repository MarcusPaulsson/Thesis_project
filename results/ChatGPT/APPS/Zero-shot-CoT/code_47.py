def max_beauty(n, x, a):
    # Function to calculate maximum subarray sum using Kadane's algorithm
    def kadane(arr):
        max_ending_here = max_so_far = 0
        for value in arr:
            max_ending_here = max(0, max_ending_here + value)
            max_so_far = max(max_so_far, max_ending_here)
        return max_so_far

    # Calculate the original beauty of the array
    original_beauty = kadane(a)

    # If x is 0, the best we can do is the original beauty
    if x == 0:
        return original_beauty

    # Calculate the maximum beauty after multiplying a subarray by x
    max_increase = 0
    current_sum = 0
    for i in range(n):
        current_sum += a[i]
        # Calculate the potential new beauty if we multiply the current subarray by x
        potential_new_sum = current_sum * x
        max_increase = max(max_increase, potential_new_sum)
        # Reset current_sum if it becomes negative
        if current_sum < 0:
            current_sum = 0

    # Calculate the maximum beauty after the operation
    max_beauty_after_operation = original_beauty + max_increase

    return max(max_beauty_after_operation, original_beauty)

# Input reading
n, x = map(int, input().split())
a = list(map(int, input().split()))

# Output the result
print(max_beauty(n, x, a))