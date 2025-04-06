def min_operations_to_remainder(n, x, y, number):
    # The target remainder in the last x digits
    target = ['0'] * x
    target[y] = '1'  # Set the y-th position to 1 for 10^y
    
    # Get the current last x digits of the number
    current = list(number[-x:])
    
    # Count the number of differences
    operations = sum(1 for i in range(x) if current[i] != target[i])
    
    return operations

# Read input
n, x, y = map(int, input().split())
number = input().strip()

# Get the result
result = min_operations_to_remainder(n, x, y, number)

# Print the result
print(result)