def max_subarray_sum(arr):
    max_sum = 0
    current_sum = 0
    for num in arr:
        current_sum += num
        if current_sum < 0:
            current_sum = 0
        max_sum = max(max_sum, current_sum)
    return max_sum

def max_beauty_with_multiplier(n, x, a):
    # Calculate the original beauty of the array
    original_beauty = max_subarray_sum(a)
    
    # If x is 0, the best we can do is the original beauty
    if x == 0:
        return original_beauty
    
    # Calculate the maximum beauty after applying the multiplier
    max_beauty = original_beauty
    for i in range(n):
        for j in range(i, n):
            # Create a new array with the subarray [i:j] multiplied by x
            modified_array = a[:i] + [a[k] * x for k in range(i, j + 1)] + a[j + 1:]
            max_beauty = max(max_beauty, max_subarray_sum(modified_array))
    
    return max_beauty

# Input reading
n, x = map(int, input().split())
a = list(map(int, input().split()))

# Get the result and print it
result = max_beauty_with_multiplier(n, x, a)
print(result)