n = int(input())
s = input()

min_operations = n  # Start with the maximum operations (typing each character)
for i in range(1, n):
    if s[:i] == s[i:i+i]:  # Check if the prefix can be copied
        min_operations = min(min_operations, i + 1 + (n - (i * 2)))  # Type i characters, copy, then type the rest

print(min_operations)