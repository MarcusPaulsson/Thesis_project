n, x, y = map(int, input().split())
number = input().strip()

# We need to check the last x digits of the number
target = ['0'] * x
target[y] = '1'  # We want the y-th position to be 1
target = ''.join(target)

# Get the last x digits of the number
current = number[-x:]

# Count the number of changes needed
operations = sum(1 for i in range(x) if current[i] != target[i])

print(operations)