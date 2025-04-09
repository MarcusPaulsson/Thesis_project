def max_beauty_with_multiplier(n, x, a):
    # Function to calculate maximum subarray sum using Kadane's algorithm
    def kadane(arr):
        max_ending_here = 0
        max_so_far = 0
        for value in arr:
            max_ending_here = max(0, max_ending_here + value)
            max_so_far = max(max_so_far, max_ending_here)
        return max_so_far

    # Calculate the original beauty of the array
    original_beauty = kadane(a)

    # If x is 0, we cannot increase the beauty, return original beauty
    if x == 0:
        return original_beauty

    # Calculate the maximum beauty after multiplying a subarray by x
    max_gain = 0
    current_sum = 0
    for value in a:
        current_sum += value
        max_gain = max(max_gain, current_sum)
        
        # If current_sum becomes negative, reset it
        if current_sum < 0:
            current_sum = 0
            
    # Calculate the effect of multiplying a subarray by x
    current_sum = 0
    for value in a:
        current_sum += value * x
        max_gain = max(max_gain, current_sum)
        
        # If current_sum becomes negative, reset it
        if current_sum < 0:
            current_sum = 0

    # The total beauty can be original beauty + max_gain
    return max(original_beauty, original_beauty + max_gain)

# Input reading
n, x = map(int, input().split())
a = list(map(int, input().split()))

# Get the result and print it
result = max_beauty_with_multiplier(n, x, a)
print(result)