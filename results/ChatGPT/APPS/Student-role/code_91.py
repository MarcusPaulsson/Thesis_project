def max_removable_length(s, t):
    n, m = len(s), len(t)
    
    # Create a prefix array to find the first occurrence of t in s
    prefix = [0] * (m + 1)
    j = 0
    for i in range(n):
        if j < m and s[i] == t[j]:
            j += 1
        prefix[j] = i + 1
    
    # Create a suffix array to find the last occurrence of t in s
    suffix = [0] * (m + 1)
    j = m - 1
    for i in range(n - 1, -1, -1):
        if j >= 0 and s[i] == t[j]:
            j -= 1
        suffix[j + 1] = i
    
    # Calculate the maximum removable length
    max_length = 0
    for i in range(m + 1):
        if prefix[i] <= suffix[i]:
            max_length = max(max_length, suffix[i] - prefix[i] + 1)
    
    return max_length

# Input reading
s = input().strip()
t = input().strip()

# Output the result
print(max_removable_length(s, t))