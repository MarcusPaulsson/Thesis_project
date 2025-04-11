n = int(input())
s = input()

min_operations = n  # Start with the maximum operations (typing all characters)

# Check for all possible prefixes to copy
for i in range(1, n):
    if s[:i] == s[i:i+i]:  # Check if the prefix can be copied
        # Operations: type prefix + copy + remaining characters
        operations = i + 1 + (n - (i * 2))
        min_operations = min(min_operations, operations)

print(min_operations)