n, x, y = map(int, input().split())
number = input().strip()

# We need to check the last x digits of the number
target_remainder = ['0'] * x
target_remainder[y] = '1'

# Count the number of changes needed
changes_needed = 0
for i in range(x):
    if number[n - 1 - i] != target_remainder[x - 1 - i]:
        changes_needed += 1

print(changes_needed)