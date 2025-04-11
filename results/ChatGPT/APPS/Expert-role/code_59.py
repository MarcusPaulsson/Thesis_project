def min_operations_to_remainder(n, x, y, number):
    # The target remainder is 10^y, which means we need the last (y+1) digits
    # to be '000...010...0' where there are y zeros followed by a 1.
    
    target = ['0'] * x
    target[y] = '1'
    
    # Count the number of changes needed
    operations = 0
    for i in range(x):
        if number[n - 1 - i] != target[x - 1 - i]:
            operations += 1
            
    return operations

# Input reading
n, x, y = map(int, input().split())
number = input().strip()

# Output the result
print(min_operations_to_remainder(n, x, y, number))