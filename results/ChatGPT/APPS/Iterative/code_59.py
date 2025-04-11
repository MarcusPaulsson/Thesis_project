n, x, y = map(int, input().split())
number = input().strip()

# Create the target remainder pattern
target_remainder = ['0'] * x
target_remainder[y] = '1'  # Set the y-th position to 1 for remainder 10^y

# Count the number of changes needed
changes = 0
for i in range(x):
    if number[n - 1 - i] != target_remainder[x - 1 - i]:
        changes += 1

print(changes)