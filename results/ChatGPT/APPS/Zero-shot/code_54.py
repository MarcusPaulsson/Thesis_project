def min_D_to_equalize(n, a):
    min_a = min(a)
    max_a = max(a)
    
    if max_a == min_a:
        return 0  # All elements are already equal
    
    # The possible target values to equalize to
    target_values = {min_a, max_a}
    
    # Check if we can equalize to any of the target values
    for target in target_values:
        D = abs(target - min_a)  # Calculate D based on the minimum value
        if all(abs(ai - target) <= D for ai in a):
            return D
    
    return -1  # If no valid D found

# Input reading
n = int(input())
a = list(map(int, input().split()))

# Output the result
print(min_D_to_equalize(n, a))