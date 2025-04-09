def max_remove_length(s, t):
    n, m = len(s), len(t)
    
    # Create two arrays to store the first match indices
    left = [0] * m
    right = [0] * m
    
    # Fill the left array
    j = 0
    for i in range(n):
        if j < m and s[i] == t[j]:
            left[j] = i
            j += 1
    
    # Fill the right array
    j = m - 1
    for i in range(n - 1, -1, -1):
        if j >= 0 and s[i] == t[j]:
            right[j] = i
            j -= 1
    
    # Now find the maximum removable length
    max_length = 0
    for i in range(m - 1):
        max_length = max(max_length, right[i + 1] - left[i] - 1)
    
    # Also consider removing from start or end
    max_length = max(max_length, right[0])  # Remove from the start to the first match of t[0]
    max_length = max(max_length, n - 1 - left[m - 1])  # Remove from the last match of t[m-1] to the end
    
    return max_length

# Input
s = input().strip()
t = input().strip()

# Output
print(max_remove_length(s, t))