n = int(input())
s = input()

# The minimum operations needed to type the string
min_operations = n

# Check for possible prefixes to copy
for i in range(1, n // 2 + 1):
    if s[:i] == s[i:2*i]:  # Check if the prefix matches the next segment
        # Calculate operations: type prefix + copy + remaining characters
        operations = i + 1 + (n - 2 * i)
        min_operations = min(min_operations, operations)

print(min_operations)