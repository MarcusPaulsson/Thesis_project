n = int(input())
s = input().strip()

min_operations = n  # Start with the assumption that we will type all characters one by one

for i in range(1, n // 2 + 1):  # Check up to half the length of the string
    if s[:i] == s[i:2*i]:  # Check if we can copy the first i characters
        operations = i + 1 + (n - 2 * i)  # i (initial characters) + 1 (copy operation) + remaining characters
        min_operations = min(min_operations, operations)

print(min_operations)