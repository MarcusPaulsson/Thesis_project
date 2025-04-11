n = int(input())
s = input()

# Initialize the minimum operations to the length of the string (typing all characters one by one)
min_operations = n

# Check for all possible prefixes
for i in range(1, n):
    # Check if the prefix can be doubled and still fit in the string
    if s[:i] == s[i:i+i] and i + i <= n:
        # Calculate operations: type prefix + copy + remaining characters
        operations = i + 1 + (n - (i + i))
        min_operations = min(min_operations, operations)

# Print the minimum operations found
print(min_operations)