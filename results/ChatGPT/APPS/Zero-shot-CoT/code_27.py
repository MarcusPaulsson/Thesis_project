n = int(input())
s = input().strip()

min_operations = n  # Start with the assumption that typing all characters one by one is the minimum

for i in range(1, n):
    if s[:i] == s[i:2*i]:  # Check if the prefix is the same as the next segment
        # Calculate the operations: type the first i characters, copy, and type the rest
        operations = i + 1 + (n - 2 * i)
        min_operations = min(min_operations, operations)

print(min_operations)