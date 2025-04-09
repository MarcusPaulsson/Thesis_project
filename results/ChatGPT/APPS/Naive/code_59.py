def min_operations(n, x, y, number):
    # The length of the number is n
    # We need to ensure the last x digits of the number give remainder 10^y
    
    # The target pattern
    target = ['0'] * x
    target[y] = '1'  # Set the y-th position to 1 as required
    
    # Count operations needed
    operations = 0
    
    # We only need to check the last x digits of the number
    for i in range(x):
        if number[n - 1 - i] != target[x - 1 - i]:
            operations += 1
            
    return operations

# Input reading
n, x, y = map(int, input().split())
number = input().strip()

# Calculate and print the result
result = min_operations(n, x, y, number)
print(result)