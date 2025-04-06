n, x, y = map(int, input().split())
number = input().strip()

# We need the last x digits to be '000...010...0' where there are y zeros followed by a one
target = ['0'] * x
target[y] = '1'

# Count the number of changes needed
changes = 0
for i in range(x):
    if number[n - 1 - i] != target[x - 1 - i]:
        changes += 1

print(changes)