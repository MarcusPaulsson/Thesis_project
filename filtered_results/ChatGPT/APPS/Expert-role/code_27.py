n = int(input())
s = input()

# Initialize the minimum operations with the case of typing all characters one by one
min_operations = n

# Check for every possible prefix length to see if we can benefit from copying
for i in range(1, n):
    # If the prefix is equal to the substring starting from that point
    if s[:i] == s[i:i + i]:  # Check if we can copy the prefix
        # Calculate operations: type the prefix (i) + copy (1) + remaining characters (n - 2*i)
        operations = i + 1 + (n - 2 * i)
        min_operations = min(min_operations, operations)

# Print the minimum operations found
print(min_operations)