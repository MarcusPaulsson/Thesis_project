n, x, y = map(int, input().split())
number = input().strip()

# We need to ensure that the last y digits are 0s and the digit at position y (counting from 0) is 1
# The last x digits should be 0s except for the y-th digit which should be 1

# Count the number of changes needed
changes = 0

# Check the last y digits for 0s
for i in range(y):
    if number[n - 1 - i] != '0':
        changes += 1

# Check the y-th digit for 1
if number[n - 1 - y] != '1':
    changes += 1

# Check the remaining (x - y - 1) digits for 0s
for i in range(y + 1, x):
    if number[n - 1 - i] != '0':
        changes += 1

print(changes)