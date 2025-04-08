def min_operations_to_remainder(n, x, y, decimal_number):
    # Define the target pattern based on y and x
    target_pattern = '0' * y + '1' + '0' * (x - y - 1)
    
    # Extract the relevant portion of the number (last x digits)
    relevant_part = decimal_number[-x:]
    
    # Count the number of operations needed to match the target pattern
    operations_needed = sum(1 for i in range(x) if relevant_part[i] != target_pattern[i])
    
    return operations_needed

# Read input values
n, x, y = map(int, input().split())
decimal_number = input().strip()

# Print the result of the minimum operations needed
print(min_operations_to_remainder(n, x, y, decimal_number))