def min_operations(n, s):
    # Initialize the minimum operations to the length of the string
    min_ops = n
    
    # Check for all possible prefixes
    for i in range(1, n + 1):
        prefix = s[:i]
        # Check if the prefix can be repeated to form the beginning of the string
        if s.startswith(prefix * (n // i)) and n % i == 0:
            # Calculate operations: typing the prefix + 1 copy + remaining characters
            operations = i + 1 + (n - len(prefix * (n // i)))
            min_ops = min(min_ops, operations)
    
    return min_ops

# Input reading
n = int(input())
s = input().strip()

# Output the result
print(min_operations(n, s))