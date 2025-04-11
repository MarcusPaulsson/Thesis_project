def min_operations(n, s):
    # Start with the assumption that we will type each character one by one
    min_ops = n
    
    # Check for possible copy operations
    for i in range(1, n // 2 + 1):
        # Check if the substring s[0:i] can be repeated to form the prefix of s
        if s[:i] == s[i:2*i] and 2*i <= n:
            # Calculate operations: type i characters, copy, and type the remaining characters
            remaining_chars = n - 2 * i
            min_ops = min(min_ops, i + 1 + remaining_chars)
    
    return min_ops

# Input reading
n = int(input())
s = input()

# Output the result
print(min_operations(n, s))