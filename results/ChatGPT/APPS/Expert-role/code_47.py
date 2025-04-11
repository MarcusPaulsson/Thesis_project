def max_beauty(n, x, a):
    # Function to calculate the maximum subarray sum using Kadane's algorithm
    def kadane(arr):
        max_sum = 0
        current_sum = 0
        for value in arr:
            current_sum += value
            max_sum = max(max_sum, current_sum)
            current_sum = max(current_sum, 0)
        return max_sum

    # Calculate the original beauty of the array
    original_beauty = kadane(a)

    # If x is 0, we can only take the original beauty
    if x == 0:
        return original_beauty

    # Calculate the maximum beauty after multiplying a subarray by x
    max_increase = 0
    current_sum = 0
    for i in range(n):
        current_sum += a[i]
        # Calculate the potential increase if we multiply the subarray ending at i
        potential_increase = current_sum * (x - 1)
        max_increase = max(max_increase, potential_increase)
        # Reset current_sum if it drops below 0
        if current_sum < 0:
            current_sum = 0

    # The maximum beauty after the operation
    return max(original_beauty, original_beauty + max_increase)

# Input reading
n, x = map(int, input().split())
a = list(map(int, input().split()))

# Output the result
print(max_beauty(n, x, a))