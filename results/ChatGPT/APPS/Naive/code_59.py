def min_operations_to_remainder(n, x, y, number):
    # Calculate the target pattern based on y
    target = ['0'] * x
    target[y] = '1'
    
    # Count the number of changes needed
    changes = 0
    for i in range(x):
        if number[n - 1 - i] != target[x - 1 - i]:
            changes += 1
            
    return changes

# Read input
n, x, y = map(int, input().split())
number = input().strip()

# Get the result and print it
result = min_operations_to_remainder(n, x, y, number)
print(result)