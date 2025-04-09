n, x, y = map(int, input().split())
number = input().strip()

# Create the target suffix based on y
target_suffix = ['0'] * x
target_suffix[y] = '1'
target_suffix = ''.join(target_suffix)

# Get the current suffix from the number
current_suffix = number[-x:]

# Calculate the number of operations needed
min_operations = sum(1 for i in range(x) if current_suffix[i] != target_suffix[i])

print(min_operations)