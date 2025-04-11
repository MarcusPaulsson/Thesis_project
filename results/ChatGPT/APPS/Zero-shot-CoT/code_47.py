def max_beauty_with_subarray(n, x, a):
    # Function to calculate maximum subarray sum using Kadane's algorithm
    def kadane(arr):
        max_ending_here = max_so_far = 0
        for value in arr:
            max_ending_here = max(0, max_ending_here + value)
            max_so_far = max(max_so_far, max_ending_here)
        return max_so_far

    # Calculate the beauty of the original array
    original_beauty = kadane(a)

    # If x is 0, multiplying any subarray will not help, return original beauty
    if x == 0:
        return original_beauty

    # Calculate the maximum beauty after multiplying a subarray by x
    max_gain = 0
    current_gain = 0

    for i in range(n):
        current_gain += a[i] * (x - 1)
        max_gain = max(max_gain, current_gain)
        if current_gain < 0:
            current_gain = 0

    # The maximum beauty will be the maximum of original beauty and the beauty after the best subarray multiplication
    return max(original_beauty, original_beauty + max_gain)

# Read input
n, x = map(int, input().split())
a = list(map(int, input().split()))

# Get the result and print it
result = max_beauty_with_subarray(n, x, a)
print(result)