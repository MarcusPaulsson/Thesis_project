def max_beauty_with_multiplier(n, x, a):
    # Function to calculate maximum subarray sum using Kadane's algorithm
    def kadane(arr):
        max_ending_here = max_so_far = 0
        for value in arr:
            max_ending_here = max(0, max_ending_here + value)
            max_so_far = max(max_so_far, max_ending_here)
        return max_so_far

    # Calculate the original beauty of the array
    original_beauty = kadane(a)

    # Calculate the maximum beauty after multiplying a subarray by x
    max_gain = 0
    current_gain = 0

    for i in range(n):
        current_gain += a[i] * (x - 1)
        if current_gain < 0:
            current_gain = 0
        max_gain = max(max_gain, current_gain)

    # The maximum beauty is either the original beauty or the beauty after applying the multiplier
    return max(original_beauty, original_beauty + max_gain)

# Read input
n, x = map(int, input().split())
a = list(map(int, input().split()))

# Get the result and print it
result = max_beauty_with_multiplier(n, x, a)
print(result)