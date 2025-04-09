n = int(input())
s = input()

min_operations = n  # Start with the max operations (typing all characters one by one)

for i in range(1, n):
    if s[:i] == s[i:2*i]:  # Check if the prefix is equal to the next segment
        # If they are equal, we can copy and then type the rest
        min_operations = min(min_operations, i + 1 + (n - 2 * i))

print(min_operations)