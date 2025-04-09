n, x, y = map(int, input().split())
number = input().strip()

# We need to check the last x digits of the number
target = ['0'] * x
target[y] = '1'  # We want to set the y-th digit to 1
target = ''.join(target)

# Get the last x digits from the number
current = number[-x:]

# Count the number of changes required
changes = sum(1 for i in range(x) if current[i] != target[i])

print(changes)