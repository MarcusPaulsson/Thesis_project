n = int(input())
s = input()

min_operations = n  # Start with the assumption that we type all characters one by one

for i in range(1, n):
    if s[:i] == s[i:i+i]:  # Check if the prefix can be copied
        min_operations = min(min_operations, i + 1 + (n - 2 * i))

print(min_operations)