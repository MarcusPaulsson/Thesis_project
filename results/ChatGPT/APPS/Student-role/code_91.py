def max_removable_length(s, t):
    n, m = len(s), len(t)
    
    # Create a prefix array to find the first occurrence of t in s
    prefix = [0] * m
    j = 0
    for i in range(n):
        if j < m and s[i] == t[j]:
            prefix[j] = i
            j += 1
    
    # Create a suffix array to find the last occurrence of t in s
    suffix = [0] * m
    j = m - 1
    for i in range(n - 1, -1, -1):
        if j >= 0 and s[i] == t[j]:
            suffix[j] = i
            j -= 1
    
    # Calculate the maximum removable length
    max_length = 0
    for i in range(m - 1):
        max_length = max(max_length, suffix[i + 1] - prefix[i] - 1)
    
    # Consider removing from the start or the end
    max_length = max(max_length, suffix[0])  # Remove from the start
    max_length = max(max_length, n - 1 - prefix[m - 1])  # Remove from the end
    
    return max_length

s = input().strip()
t = input().strip()
print(max_removable_length(s, t))