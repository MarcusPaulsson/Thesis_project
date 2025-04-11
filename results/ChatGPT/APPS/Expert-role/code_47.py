def max_beauty(n, x, a):
    # Function to calculate the maximum subarray sum using Kadane's algorithm
    def kadane(arr):
        max_ending_here = max_so_far = 0
        for value in arr:
            max_ending_here = max(0, max_ending_here + value)
            max_so_far = max(max_so_far, max_ending_here)
        return max_so_far

    # Calculate the beauty of the original array
    original_beauty = kadane(a)

    # If x is 1, multiplying by x doesn't change the array
    if x == 1:
        return original_beauty

    # Calculate the maximum beauty after multiplying a subarray by x
    max_with_x = 0
    current_sum = 0

    for i in range(n):
        current_sum += a[i]
        max_with_x = max(max_with_x, current_sum * x)
        current_sum = max(current_sum, 0)

    # Now we need to consider the case where we multiply a subarray by x
    # We will calculate the maximum sum of the array after applying the multiplication
    max_sum_with_x = 0
    current_sum = 0

    for i in range(n):
        current_sum += a[i]
        max_sum_with_x = max(max_sum_with_x, current_sum)
        current_sum = max(current_sum, 0)

    # Now we need to consider the case where we multiply a subarray by x
    max_sum_with_x = max(max_sum_with_x, original_beauty + max_with_x)

    return max(original_beauty, max_sum_with_x)

# Input reading
n, x = map(int, input().split())
a = list(map(int, input().split()))

# Output the result
print(max_beauty(n, x, a))