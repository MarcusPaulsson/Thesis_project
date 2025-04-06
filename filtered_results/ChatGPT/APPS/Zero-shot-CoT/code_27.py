n = int(input())
s = input().strip()

min_operations = n  # Start with the assumption that we need to type all characters one by one

# Check for every possible length to copy
for i in range(1, n // 2 + 1):
    if s[:i] == s[i:2 * i]:  # Check if the first i characters are the same as the next i characters
        # If they are equal, we can copy and then type the rest
        total_length = 2 * i
        remaining_length = n - total_length
        operations = i + 1 + remaining_length  # i (type first part) + 1 (copy) + remaining_length (type remaining)
        min_operations = min(min_operations, operations)

# Output the minimum operations found
print(min_operations)