def min_operations_to_remainder(n, x, y, num_str):
    # Calculate the required pattern for the last x digits
    required_pattern = ['0'] * x
    required_pattern[y] = '1'  # Set the y-th position to 1 for the remainder 10^y
    required_pattern = ''.join(required_pattern)
    
    # Get the last x digits of the input number
    current_suffix = num_str[-x:]
    
    # Count the number of changes required
    operations = 0
    for i in range(x):
        if current_suffix[i] != required_pattern[i]:
            operations += 1
    
    return operations

# Input reading
n, x, y = map(int, input().split())
num_str = input().strip()

# Calculate and print the result
result = min_operations_to_remainder(n, x, y, num_str)
print(result)