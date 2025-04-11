n, x, y = map(int, input().split())
number = input().strip()

# The target remainder is 10^y, which means we need the last (y+1) digits to be '0' and the (y+1)th digit to be '1'
# The last x digits of the number
last_x_digits = number[-x:]

# We need to change the last (y) digits to '0' and the (y+1)th digit to '1'
changes_needed = 0

# Check the last (y) digits (from index -1 to -y)
for i in range(1, y + 1):
    if last_x_digits[-i] != '0':
        changes_needed += 1

# Check the (y+1)th digit (which is at index -y-1)
if last_x_digits[-(y + 1)] != '1':
    changes_needed += 1

print(changes_needed)