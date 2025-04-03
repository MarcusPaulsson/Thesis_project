def max_beauty_with_subarray(n, x, a):
    # Function to calculate the maximum subarray sum using Kadane's algorithm
    def kadane(arr):
        max_ending_here = max_so_far = 0
        for value in arr:
            max_ending_here = max(0, max_ending_here + value)  # Allow empty subarray
            max_so_far = max(max_so_far, max_ending_here)
        return max_so_far

    # Calculate the original beauty
    original_beauty = kadane(a)

    # If x is 1, multiplying by x doesn't change the array
    if x == 1:
        return original_beauty

    # Calculate the effect of multiplying a subarray by x
    max_increase = 0  # Maximum increase from multiplying a subarray by x
    current_sum = 0
    max_subarray_sum = 0

    for value in a:
        current_sum += value
        max_subarray_sum = max(max_subarray_sum, current_sum)
        
        # Calculate the potential new beauty if this subarray is multiplied by x
        potential_new_sum = current_sum * (x - 1)
        max_increase = max(max_increase, potential_new_sum)
        
        # Reset current_sum if it falls below 0 (Kadane's logic)
        if current_sum < 0:
            current_sum = 0

    # The new beauty would be the original beauty plus the best increase we could get
    return max(original_beauty, original_beauty + max_increase)

# Read input
n, x = map(int, input().split())
a = list(map(int, input().split()))

# Print the result
print(max_beauty_with_subarray(n, x, a))