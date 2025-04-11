n, x, y = map(int, input().split())
number = input().strip()

# We need to check the last x digits of the number
target_remainder = '0' * (x - y - 1) + '1' + '0' * y  # This is the desired pattern
current_remainder = number[-x:]  # The last x digits of the number

# Count the number of changes needed
operations = sum(1 for i in range(x) if current_remainder[i] != target_remainder[i])

print(operations)