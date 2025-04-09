def max_removable_length(s, t):
    n, m = len(s), len(t)
    
    # Arrays to store the positions of characters in s that match t
    left = [0] * m
    right = [0] * m
    
    # Fill left array for the first occurrence
    j = 0
    for i in range(n):
        if j < m and s[i] == t[j]:
            left[j] = i
            j += 1
    
    # Fill right array for the last occurrence
    j = m - 1
    for i in range(n - 1, -1, -1):
        if j >= 0 and s[i] == t[j]:
            right[j] = i
            j -= 1
    
    # Calculate the maximum removable length
    max_length = 0
    for i in range(m - 1):
        max_length = max(max_length, right[i + 1] - left[i] - 1)
    
    # Also consider removing from the start to the first character of t
    max_length = max(max_length, right[0] - 0)
    # And from the last character of t to the end of s
    max_length = max(max_length, n - left[m - 1] - 1)
    
    return max_length

# Input
s = input().strip()
t = input().strip()

# Output
print(max_removable_length(s, t))