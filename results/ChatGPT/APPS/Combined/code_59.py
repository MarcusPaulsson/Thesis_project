def min_operations_to_remainder(n, x, y, number):
    # Create the target pattern with '0's and a '1' at the y-th position
    target = ['0'] * x
    target[y] = '1'
    
    # Count the number of changes needed
    changes_needed = sum(1 for i in range(x) if number[n - 1 - i] != target[x - 1 - i])
    
    return changes_needed

# Read input
n, x, y = map(int, input().split())
number = input().strip()

# Calculate and print the result
result = min_operations_to_remainder(n, x, y, number)
print(result)