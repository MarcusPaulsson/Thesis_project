def max_subarray_sum(arr):
    max_ending_here = 0
    max_so_far = 0
    for x in arr:
        max_ending_here = max(0, max_ending_here + x)
        max_so_far = max(max_so_far, max_ending_here)
    return max_so_far

def max_beauty_after_operation(n, x, a):
    # Calculate the original beauty
    original_beauty = max_subarray_sum(a)

    # Initialize variables for the modified beauty calculation
    max_increase = 0
    current_sum = 0
    total_sum = sum(a)

    # Iterate through the array to find the best subarray to multiply
    for i in range(n):
        current_sum += a[i]
        
        # If we multiply the current sum by x
        if x != 0:
            modified_sum = current_sum * x
            # Calculate the increase in beauty
            increase = modified_sum - current_sum
            max_increase = max(max_increase, increase)

        # Reset current_sum if it becomes negative
        if current_sum < 0:
            current_sum = 0

    # The maximum beauty after the operation
    max_beauty = max(original_beauty, total_sum + max_increase)
    return max_beauty

# Input
n, x = map(int, input().split())
a = list(map(int, input().split()))

# Output the result
print(max_beauty_after_operation(n, x, a))