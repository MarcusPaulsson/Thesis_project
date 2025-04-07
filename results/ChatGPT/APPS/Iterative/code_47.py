def max_subarray_sum(arr):
    max_sum = 0
    current_sum = 0
    for num in arr:
        current_sum = max(0, current_sum + num)
        max_sum = max(max_sum, current_sum)
    return max_sum

def max_beauty_after_operation(n, x, a):
    original_beauty = max_subarray_sum(a)
    
    if x <= 0:
        return original_beauty
    
    max_gain = 0
    current_gain = 0
    for i in range(n):
        potential_gain = a[i] * (x - 1)
        current_gain += potential_gain
        max_gain = max(max_gain, current_gain)
        if current_gain < 0:
            current_gain = 0
    
    return original_beauty + max_gain

# Input reading
n, x = map(int, input().split())
a = list(map(int, input().split()))

# Calculate and print the result
print(max_beauty_after_operation(n, x, a))