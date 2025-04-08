def min_operations(n, s):
    # Initially, the minimum operations is the length of the string (typing all characters)
    min_ops = n
    
    # Iterate through possible lengths of the prefix to copy
    for i in range(1, n // 2 + 1):
        # Check if the substring can be doubled and is a prefix of the entire string
        if s[:i] == s[i:2*i]:
            # Calculate operations: type i characters, copy, and type the remaining characters
            ops = i + 1 + (n - 2 * i)
            min_ops = min(min_ops, ops)
    
    return min_ops

# Input reading
n = int(input())
s = input().strip()

# Output the result
print(min_operations(n, s))