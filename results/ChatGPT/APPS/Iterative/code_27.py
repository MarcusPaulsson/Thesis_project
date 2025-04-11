n = int(input())
s = input()

min_operations = n  # Start with the maximum operations (typing all characters)

# Check for all possible prefixes
for i in range(1, n + 1):
    prefix = s[:i]
    # Check if the string can be formed by prefix + copy + remaining characters
    if s.startswith(prefix * 2):
        # If we can copy the prefix, we need to type i characters, then 1 copy, then the remaining characters
        operations = i + 1 + (n - 2 * i)
        min_operations = min(min_operations, operations)

# Output the minimum operations found
print(min_operations)