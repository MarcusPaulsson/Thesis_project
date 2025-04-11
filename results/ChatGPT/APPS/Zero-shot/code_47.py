def max_subarray_sum(arr):
    max_ending_here = max_so_far = 0
    for x in arr:
        max_ending_here = max(0, max_ending_here + x)
        max_so_far = max(max_so_far, max_ending_here)
    return max_so_far

def max_beauty_with_multiplier(n, x, a):
    # Calculate the original beauty
    original_beauty = max_subarray_sum(a)
    
    # If x is 0, the best we can do is the original beauty
    if x == 0:
        return original_beauty

    # Calculate the maximum beauty after applying the multiplier
    max_with_multiplier = original_beauty
    for i in range(n):
        current_sum = 0
        for j in range(i, n):
            current_sum += a[j]
            # Calculate the new beauty if we multiply the subarray a[i:j+1] by x
            new_sum = current_sum * x
            # Calculate the beauty of the rest of the array
            rest_sum = max_subarray_sum(a[:i] + a[j+1:])
            max_with_multiplier = max(max_with_multiplier, new_sum + rest_sum)

    return max_with_multiplier

# Input reading
n, x = map(int, input().split())
a = list(map(int, input().split()))

# Output the result
print(max_beauty_with_multiplier(n, x, a))