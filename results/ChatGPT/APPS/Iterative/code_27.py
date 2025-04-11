n = int(input())
s = input()

min_operations = n  # Start with the maximum operations (typing all characters)

for i in range(1, n // 2 + 1):
    if s[:i] == s[i:2*i]:  # Check if the prefix can be copied
        # Calculate operations: type i characters, copy, and type the rest
        operations = i + 1 + (n - 2 * i)
        min_operations = min(min_operations, operations)

# If the string length is odd, we need to consider typing all characters
if n % 2 == 1:
    min_operations = min(min_operations, n)

print(min_operations)