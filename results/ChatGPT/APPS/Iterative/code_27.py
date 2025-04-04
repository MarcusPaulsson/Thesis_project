n = int(input())
s = input().strip()

# Initialize the minimum operations to n (typing all characters one by one)
min_operations = n

# Try every possible split to find the best copy point
for i in range(1, n):
    # The prefix we are considering to copy
    prefix = s[:i]
    # The next part of the string after the prefix
    remaining = s[i:]

    # Check if the remaining string starts with the prefix
    if remaining.startswith(prefix):
        # Calculate the required operations
        operations = i + 1 + (len(remaining) - len(prefix))
        min_operations = min(min_operations, operations)

# Output the minimum operations found
print(min_operations)