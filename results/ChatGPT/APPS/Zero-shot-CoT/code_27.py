n = int(input())
s = input()

min_operations = n  # Start with the maximum operations needed (typing all characters)

# Check for possible copy operations
for i in range(1, n):
    if s[:i] == s[i:i+i]:  # Check if the prefix can be copied
        # Calculate operations: type prefix + 1 copy + remaining characters
        operations = i + 1 + (n - 2 * i)
        min_operations = min(min_operations, operations)

print(min_operations)