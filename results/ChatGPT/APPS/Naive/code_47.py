def max_beauty_with_multiplier(n, x, a):
    # Function to calculate the maximum subarray sum using Kadane's algorithm
    def kadane(arr):
        max_sum, current_sum = 0, 0
        for value in arr:
            current_sum = max(0, current_sum + value)
            max_sum = max(max_sum, current_sum)
        return max_sum

    # Calculate the base beauty (maximum sum of any subarray without modification)
    base_beauty = kadane(a)

    # To store the maximum beauty after multiplying a subarray by x
    max_beauty = base_beauty

    # Try to find the maximum beauty after multiplying any subarray by x
    for i in range(n):
        current_sum = 0  # Sum of the current subarray
        for j in range(i, n):
            current_sum += a[j]
            # Calculate the beauty with the subarray a[i:j+1] multiplied by x
            modified_sum = current_sum * x
            new_total = modified_sum + kadane(a[:i]) + kadane(a[j + 1:])
            max_beauty = max(max_beauty, new_total)

    return max_beauty

# Reading input
n, x = map(int, input().split())
a = list(map(int, input().split()))

# Getting the maximum beauty after applying the operation
result = max_beauty_with_multiplier(n, x, a)

# Output the result
print(result)