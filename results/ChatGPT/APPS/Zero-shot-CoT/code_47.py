def max_beauty_with_multiplier(n, x, a):
    def kadane(arr):
        max_ending_here = max_so_far = 0
        for num in arr:
            max_ending_here = max(0, max_ending_here + num)
            max_so_far = max(max_so_far, max_ending_here)
        return max_so_far

    # Calculate the beauty of the array without any operation
    max_beauty = kadane(a)

    # If x is 1 or 0, multiplying won't help, return the current max_beauty
    if x >= 1:
        return max_beauty

    # Calculate the effect of multiplying subarrays by x
    # We will use two passes for the original array and the modified array
    # to find the maximum contribution after multiplying subarrays

    n = len(a)
    max_gain = 0
    prefix_sum = 0
    
    for i in range(n):
        prefix_sum += a[i]
        max_gain = max(max_gain, prefix_sum * (x - 1))
        if prefix_sum < 0:
            prefix_sum = 0

    # Now, we need to find the max contribution from the array after applying x
    # Use the Kadane's algorithm again for the original array
    # and for the modified array when multiplied by x
    max_gain_with_multiplier = kadane([a[i] * x for i in range(n)])

    # The final maximum beauty is the best of the original or modified values
    return max(max_beauty, max_gain + max_gain_with_multiplier)

# Input reading
n, x = map(int, input().split())
a = list(map(int, input().split()))

# Output the result
print(max_beauty_with_multiplier(n, x, a))