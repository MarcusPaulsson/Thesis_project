n = int(input())
s = input()

# Initialize the minimum operations to the length of the string (typing all characters one by one)
min_operations = n

# Check for possible copy operations
for i in range(1, n):
    # If the prefix of length i is equal to the suffix of length i
    if s[:i] == s[i:2*i]:
        # Calculate the operations: type i characters, copy, and type the remaining characters
        operations = i + 1 + (n - 2 * i)
        min_operations = min(min_operations, operations)

print(min_operations)