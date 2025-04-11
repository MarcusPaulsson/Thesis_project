def min_operations_to_remainder(n, x, y, number):
    # Construct the target pattern for the last x digits
    target_remainder = '0' * (x - y - 1) + '1' + '0' * y
    current_remainder = number[-x:]  # Get the last x digits of the number
    
    # Count the number of changes needed
    operations_needed = sum(1 for i in range(x) if current_remainder[i] != target_remainder[i])
    
    return operations_needed

# Input reading
n, x, y = map(int, input().split())
number = input().strip()

# Calculate and print the result
result = min_operations_to_remainder(n, x, y, number)
print(result)