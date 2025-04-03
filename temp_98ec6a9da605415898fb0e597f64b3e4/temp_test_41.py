def max_remove_length(s, t):
    n, m = len(s), len(t)
    
    # Precompute the first occurrence of each character in t
    left = [-1] * m
    j = 0
    for i in range(n):
        if j < m and s[i] == t[j]:
            left[j] = i
            j += 1
            
    # Precompute the last occurrence of each character in t
    right = [-1] * m
    j = m - 1
    for i in range(n - 1, -1, -1):
        if j >= 0 and s[i] == t[j]:
            right[j] = i
            j -= 1
    
    # Calculate the maximum removable length
    max_length = 0
    for i in range(m - 1):
        if left[i] != -1 and right[i + 1] != -1 and left[i] < right[i + 1]:
            max_length = max(max_length, right[i + 1] - left[i] - 1)
    
    # Check for the case where we can remove up to the first character of t
    if right[0] != -1:
        max_length = max(max_length, right[0] + 1)
    
    # Check for the case where we can remove from the last character of t
    if left[m - 1] != -1:
        max_length = max(max_length, n - left[m - 1] - 1)
    
    return max_length

# Input reading
s = input().strip()
t = input().strip()

# Output the result
print(max_remove_length(s, t))