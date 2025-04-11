def min_operations_to_remainder(n, x, y, number):
    # Calculate the target pattern based on y
    target = ['0'] * x
    target[y] = '1'
    
    # Count the number of operations needed
    operations = 0
    for i in range(x):
        if number[n - 1 - i] != target[x - 1 - i]:
            operations += 1
            
    return operations

# Input reading
n, x, y = map(int, input().split())
number = input().strip()

# Calculate and print the result
result = min_operations_to_remainder(n, x, y, number)
print(result)