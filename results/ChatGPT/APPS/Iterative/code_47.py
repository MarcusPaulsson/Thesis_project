def max_beauty_with_subarray(n, x, a):
    # Calculate the maximum sum of any subarray (Kadane's algorithm)
    def kadane(arr):
        max_ending_here = max_so_far = 0
        for value in arr:
            max_ending_here = max(0, max_ending_here + value)
            max_so_far = max(max_so_far, max_ending_here)
        return max_so_far

    # Original beauty of the array
    original_beauty = kadane(a)

    # If x is 0, we can only take the original beauty
    if x == 0:
        return original_beauty

    # Calculate the maximum beauty after multiplying a subarray by x
    max_increase = 0
    current_sum = 0
    for i in range(n):
        current_sum += a[i]
        max_increase = max(max_increase, current_sum * x)
        if current_sum < 0:
            current_sum = 0

    # Calculate the maximum beauty considering the increase
    max_beauty = original_beauty + max_increase

    return max_beauty

# Input reading
n, x = map(int, input().split())
a = list(map(int, input().split()))

# Output the result
print(max_beauty_with_subarray(n, x, a))