def min_operations_to_mod(n, x, y, number):
    # The required suffix we want to match
    required_suffix = ['0'] * x
    required_suffix[y] = '1'
    
    # Current suffix from the number
    current_suffix = list(number[-x:])
    
    # Count the number of changes needed
    operations = sum(1 for i in range(x) if current_suffix[i] != required_suffix[i])
    
    return operations

# Read input
n, x, y = map(int, input().split())
number = input().strip()

# Calculate and print the result
result = min_operations_to_mod(n, x, y, number)
print(result)