n = int(input())
s = input()

min_operations = n  # Start with the assumption that we type all characters one by one

# Check for all possible prefixes to copy
for i in range(1, n):
    prefix = s[:i]
    if s.startswith(prefix, i):  # Check if the string can be formed by prefix + remaining
        # Operations: type prefix (i) + copy (1) + type remaining (n - 2*i)
        operations = i + 1 + (n - 2 * i)
        min_operations = min(min_operations, operations)

print(min_operations)