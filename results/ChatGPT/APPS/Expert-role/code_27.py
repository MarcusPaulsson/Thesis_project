n = int(input())
s = input()

# Function to find the minimum operations
def min_operations(n, s):
    # Start with typing all characters one by one
    min_ops = n
    
    # Check for every possible prefix length
    for i in range(1, n // 2 + 1):
        if s[:i] == s[i:2*i]:  # Check if the first i characters match the next i characters
            # Calculate the operations: type prefix + copy + remaining characters
            min_ops = min(min_ops, i + 1 + (n - 2 * i))
    
    return min_ops

# Print the result
print(min_operations(n, s))