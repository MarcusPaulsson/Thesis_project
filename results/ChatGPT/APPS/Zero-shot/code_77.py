n = int(input())
s = input().strip()

# Initialize the minimum operations with the case of typing all characters one by one
min_operations = n

# Check for every possible prefix to see if we can copy and append
for i in range(1, n):
    # Check if the prefix s[:i] can be repeated to cover the next part of the string
    if s[:i] == s[i:2*i] and 2*i <= n:
        # We can type i characters, then perform a copy operation, then type the remaining characters
        remaining = n - 2 * i
        min_operations = min(min_operations, i + 1 + remaining)

# Print the minimum number of operations
print(min_operations)