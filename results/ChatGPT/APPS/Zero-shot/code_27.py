n = int(input())
s = input()

min_operations = n  # Initialize with the maximum operations (typing all characters)

# Check possible places to copy the string
for i in range(1, n):
    if s[:i] == s[i:2*i]:  # Check if the substring can be copied
        copy_length = i
        remaining_length = n - 2 * copy_length
        operations = copy_length + 1 + remaining_length  # Type, copy, type remaining
        min_operations = min(min_operations, operations)

# Check if we can type the whole string without copying
min_operations = min(min_operations, n)

print(min_operations)