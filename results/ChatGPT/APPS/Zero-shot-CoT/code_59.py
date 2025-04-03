n, x, y = map(int, input().split())
number = input().strip()

# Calculate the target remainder which is 10^y
target = ['0'] * x
target[y] = '1'

# We need to compare the last x digits of the number with the target
current = number[-x:]

# Count the number of operations needed
operations = 0
for i in range(x):
    if current[i] != target[i]:
        operations += 1

print(operations)