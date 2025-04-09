def max_removable_length(s, t):
    n = len(s)
    m = len(t)
    
    # Precompute the prefix indices of t in s
    prefix = [0] * m
    j = 0
    for i in range(n):
        if j < m and s[i] == t[j]:
            prefix[j] = i
            j += 1
    
    # Precompute the suffix indices of t in s
    suffix = [0] * m
    j = m - 1
    for i in range(n - 1, -1, -1):
        if j >= 0 and s[i] == t[j]:
            suffix[j] = i
            j -= 1
    
    # Find the maximum removable length
    max_length = 0
    for i in range(m - 1):
        max_length = max(max_length, suffix[i + 1] - prefix[i] - 1)
    
    # Consider removing from the start to the first character of t
    max_length = max(max_length, suffix[0])  # Remove everything before the first character of t
    # Consider removing from the last character of t to the end
    max_length = max(max_length, n - 1 - prefix[m - 1])  # Remove everything after the last character of t
    
    return max_length

# Read input
s = input().strip()
t = input().strip()

# Get result and print it
result = max_removable_length(s, t)
print(result)