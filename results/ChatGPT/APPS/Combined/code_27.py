def min_operations(n, s):
    # Initialize minimum operations to the length of the string (typing all characters)
    min_ops = n
    
    # Check for possible prefixes that can be doubled
    for i in range(1, n // 2 + 1):
        if s[:i] == s[i:2 * i]:
            # Calculate operations: typing the prefix + 1 for copy + remaining characters
            min_ops = min(min_ops, i + 1 + (n - 2 * i))
    
    return min_ops

# Input reading
n = int(input().strip())
s = input().strip()

# Output the result
print(min_operations(n, s))