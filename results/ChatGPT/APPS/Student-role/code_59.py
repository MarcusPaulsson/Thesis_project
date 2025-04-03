def min_operations(n, x, y, number):
    # Target remainder is 10^y, which means we need to have the y-th position as '1'
    # and all positions from y+1 to x-1 as '0'
    target = ['0'] * x
    target[y] = '1'
    
    # Count the number of changes needed
    changes = 0
    for i in range(x):
        if number[n - 1 - i] != target[x - 1 - i]:
            changes += 1
            
    return changes

# Input reading
n, x, y = map(int, input().split())
number = input().strip()

# Output the result
print(min_operations(n, x, y, number))