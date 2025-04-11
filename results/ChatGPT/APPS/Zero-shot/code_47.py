def max_beauty(n, x, a):
    # Function to calculate maximum subarray sum using Kadane's algorithm
    def kadane(arr):
        max_ending_here = max_so_far = 0
        for value in arr:
            max_ending_here = max(0, max_ending_here + value)
            max_so_far = max(max_so_far, max_ending_here)
        return max_so_far

    # Calculate the beauty of the original array
    original_beauty = kadane(a)

    # If x is 0, the best we can do is the original beauty
    if x == 0:
        return original_beauty

    # Calculate the maximum beauty after multiplying a subarray by x
    max_increase = 0
    current_sum = 0

    for i in range(n):
        current_sum += a[i]
        # Calculate the potential new sum if we multiply the current subarray by x
        new_sum = current_sum * x
        # The increase in beauty would be new_sum - current_sum
        max_increase = max(max_increase, new_sum - current_sum)
        # Reset current_sum if it goes negative
        if current_sum < 0:
            current_sum = 0

    # The maximum beauty after the operation
    return max(original_beauty, original_beauty + max_increase)

# Input reading
n, x = map(int, input().split())
a = list(map(int, input().split()))

# Output the result
print(max_beauty(n, x, a))