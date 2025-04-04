n, x, y = map(int, input().split())
number = input().strip()

# Ensure the input number is long enough
if len(number) != n:
    raise ValueError("The length of the input number does not match n.")

# Calculate the number of changes needed
changes = 0

# Check the (y + 1)th digit from the end
if number[n - (y + 1)] != '1':
    changes += 1

# Check the last y digits
for i in range(y):
    if number[n - (i + 1)] != '0':
        changes += 1

print(changes)