def max_removable_length(s, t):
    n, m = len(s), len(t)
    
    # Precompute the positions of each character in t in s
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
    
    # Calculate the maximum removable length
    max_length = 0
    for i in range(m - 1):
        max_length = max(max_length, right[i + 1] - left[i] - 1)
    
    # Consider the part before the first character of t and after the last character of t
    max_length = max(max_length, left[0])  # Before first occurrence
    max_length = max(max_length, n - 1 - right[m - 1])  # After last occurrence
    
    return max_length

# Input
s = input().strip()
t = input().strip()

# Output
print(max_removable_length(s, t))