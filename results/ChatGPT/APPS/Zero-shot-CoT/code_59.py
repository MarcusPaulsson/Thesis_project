n, x, y = map(int, input().split())
number = input().strip()

# We need to ensure that the last x digits of the number have the form:
# ...000...010...0 (where there are y zeros followed by a 1 and then (x-y-1) zeros)
# This means we need to check the last x digits of the number.

# The target pattern we want for the last x digits
target = ['0'] * x
target[y] = '1'

# Count the number of changes needed
changes = 0
for i in range(x):
    if number[n - 1 - i] != target[x - 1 - i]:
        changes += 1

print(changes)