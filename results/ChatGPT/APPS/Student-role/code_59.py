n, x, y = map(int, input().split())
number = input().strip()

# We need to check the last x digits of the number
target = ['0'] * x
target[y] = '1'  # Set the y-th position to '1'

# Count the number of changes needed
changes = 0
for i in range(x):
    if number[n - 1 - i] != target[x - 1 - i]:
        changes += 1

print(changes)