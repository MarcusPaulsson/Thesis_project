def min_operations(n, s):
    min_ops = n  # Start with the maximum operations (typing all characters)

    # Check all possible prefix lengths
    for i in range(1, n):
        # Check if the prefix can be copied
        if s[:i] == s[i:i+i]:  # Ensure the prefix matches the next segment
            # Calculate operations: type prefix + copy + remaining characters
            operations = i + 1 + (n - (i + i))
            min_ops = min(min_ops, operations)

    return min_ops

# Input reading
n = int(input())
s = input().strip()

# Output the result
print(min_operations(n, s))