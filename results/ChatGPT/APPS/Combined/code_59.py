def min_operations_to_modulo(n, x, y, number):
    # Define the target pattern based on y and x
    target_pattern = ['0'] * x
    target_pattern[y] = '1'  # Set the y-th digit from the right to '1'
    
    # Count the number of operations needed to match the target pattern
    operations = sum(1 for i in range(x) if number[n - 1 - i] != target_pattern[x - 1 - i])
    
    return operations

# Read input
n, x, y = map(int, input().split())
number = input().strip()

# Output the result
print(min_operations_to_modulo(n, x, y, number))