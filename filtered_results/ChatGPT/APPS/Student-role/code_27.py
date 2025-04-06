n = int(input())
s = input().strip()

min_operations = n  # Start with the assumption that we type everything one by one

# Check for possible copy and append scenarios
for i in range(1, n):
    if s[:i] == s[i:2*i]:
        # If the prefix matches the next part of the string
        operations = i + 1 + (n - 2 * i)  # Type i characters, copy, then type the rest
        min_operations = min(min_operations, operations)

print(min_operations)