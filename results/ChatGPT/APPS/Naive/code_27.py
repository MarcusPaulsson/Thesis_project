def min_operations(n, s):
    # The default number of operations is to type all characters
    min_ops = n
    
    # Try every possible split point
    for i in range(1, n):
        # Check if the prefix (s[:i]) can be doubled to match the beginning of the string
        if s[:i] == s[i:i+i]:
            # Calculate operations: type prefix + 1 for copy + remaining characters
            min_ops = min(min_ops, i + 1 + (n - i - i))
    
    return min_ops

# Read input
n = int(input())
s = input().strip()

# Print the result
print(min_operations(n, s))