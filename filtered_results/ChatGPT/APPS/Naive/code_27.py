def min_operations_to_type_string(n, s):
    # Initialize the minimum operations to n (typing all characters one by one)
    min_operations = n
    
    # Iterate to find the longest prefix that can be doubled
    for i in range(1, n):
        # Check if the prefix can be doubled and still fit within the string
        if s[:i] == s[i:2*i] and 2*i <= n:
            # Calculate operations: type prefix + copy + remaining characters
            operations = i + 1 + (n - 2 * i)
            min_operations = min(min_operations, operations)
    
    return min_operations

# Input reading
n = int(input())
s = input().strip()

# Output the result
print(min_operations_to_type_string(n, s))