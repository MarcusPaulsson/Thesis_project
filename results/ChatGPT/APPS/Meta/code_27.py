n = int(input())
s = input()

# Initialize the minimum operations to the maximum possible (typing all characters)
min_operations = n

# Check for every possible prefix of the string
for i in range(1, n + 1):
    prefix = s[:i]
    # Check if the string starts with the current prefix repeated
    if s.startswith(prefix * (n // i)):
        # Calculate operations: type the prefix, copy it once, and type the remainder
        operations = i + (n - i) // i + (n - i) % i
        min_operations = min(min_operations, operations)

print(min_operations)