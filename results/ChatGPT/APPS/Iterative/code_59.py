n, x, y = map(int, input().split())
number = input().strip()

# Create the target pattern: '0' * y + '1' + '0' * (x - y - 1)
target = ['0'] * x
target[y] = '1'

# Initialize a counter for the number of operations needed
operations = 0

# Check the last x digits of the number against the target pattern
for i in range(x):
    if number[n - x + i] != target[i]:
        operations += 1

print(operations)