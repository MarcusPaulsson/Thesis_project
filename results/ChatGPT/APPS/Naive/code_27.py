def min_operations(n, s):
    # Start with the assumption that we will type all characters one by one
    min_ops = n
    
    # Check for possible copy operations
    for i in range(1, n):
        # If the prefix of length i is equal to the suffix of length i
        if s[:i] == s[i:2*i]:
            # Calculate operations: type i characters, copy, and type the rest
            min_ops = min(min_ops, i + 1 + (n - 2 * i))
    
    return min_ops

# Input reading
n = int(input().strip())
s = input().strip()

# Output the result
print(min_operations(n, s))