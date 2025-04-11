n = int(input())
s = input()

min_operations = n  # Start with the maximum operations needed (typing all characters)

# Check for every possible prefix of the string
for i in range(1, n + 1):
    prefix = s[:i]
    # If the prefix can be repeated to form the beginning of the string
    if s.startswith(prefix * (n // i)) and n % i == 0:
        min_operations = min(min_operations, i + (n - i) // i)

print(min_operations)