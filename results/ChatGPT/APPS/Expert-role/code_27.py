def min_operations(n, s):
    min_ops = n  # Start with the maximum operations (typing each character)
    
    # Check for every possible prefix length
    for i in range(1, n + 1):
        prefix = s[:i]
        # Check if the string can be formed by prefix + copy + remaining characters
        if s.startswith(prefix):
            # Calculate operations: type prefix + copy + remaining characters
            operations = i + 1 + (n - 2 * i) if n >= 2 * i else i
            min_ops = min(min_ops, operations)
    
    return min_ops

# Input reading
n = int(input())
s = input().strip()

# Output the result
print(min_operations(n, s))