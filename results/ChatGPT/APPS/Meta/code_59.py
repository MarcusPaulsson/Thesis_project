n, x, y = map(int, input().split())
number = input().strip()

# We need to check the last x digits of the number
target_remainder = '0' * y + '1' + '0' * (x - y - 1)  # This is the desired pattern
current_remainder = number[n - x:]  # Get the last x digits of the number

# Calculate the number of changes needed
changes_needed = sum(1 for i in range(x) if current_remainder[i] != target_remainder[i])

print(changes_needed)