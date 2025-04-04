def max_beauty_with_subarray(n, x, a):
    # Function to calculate maximum subarray sum using Kadane's algorithm
    def kadane(arr):
        max_sum = float('-inf')
        current_sum = 0
        for value in arr:
            current_sum += value
            max_sum = max(max_sum, current_sum)
            current_sum = max(current_sum, 0)
        return max_sum

    # Calculate the original beauty of the array
    original_beauty = kadane(a)

    # To store the maximum beauty after modifying a subarray
    max_beauty = original_beauty

    # Calculate maximum sum of subarray when multiplied by x
    for i in range(n):
        current_sum = 0
        for j in range(i, n):
            current_sum += a[j]
            # Calculate modified sum with subarray a[i:j+1] multiplied by x
            modified_sum = current_sum * x + sum(a[k] for k in range(n) if not (i <= k <= j))
            # Update max beauty
            max_beauty = max(max_beauty, modified_sum)

    return max_beauty

# Read input
n, x = map(int, input().split())
a = list(map(int, input().split()))

# Get the result
result = max_beauty_with_subarray(n, x, a)

# Print the result
print(result)