def max_removable_length(s: str, t: str) -> int:
    n, m = len(s), len(t)
    
    # Create prefix and suffix arrays to track positions of t in s
    prefix = [-1] * m
    suffix = [-1] * m
    
    # Fill prefix array
    j = 0
    for i in range(n):
        if j < m and s[i] == t[j]:
            prefix[j] = i
            j += 1
            
    # Fill suffix array
    j = m - 1
    for i in range(n - 1, -1, -1):
        if j >= 0 and s[i] == t[j]:
            suffix[j] = i
            j -= 1
            
    # Calculate the maximum removable length
    max_length = 0
    for i in range(m - 1):
        if prefix[i] != -1 and suffix[i + 1] != -1:
            max_length = max(max_length, suffix[i + 1] - prefix[i] - 1)
    
    # Consider removing from the start or the end
    max_length = max(max_length, suffix[0])  # Remove from start
    max_length = max(max_length, n - 1 - prefix[m - 1])  # Remove from end
    
    return max_length