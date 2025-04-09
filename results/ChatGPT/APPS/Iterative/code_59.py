n, x, y = map(int, input().split())
number = input().strip()

# Create target substring
target = ['0'] * x
target[y] = '1'

# Count the number of operations needed
operations = 0
for i in range(x):
    if number[n - 1 - i] != target[i]:
        operations += 1

print(operations)