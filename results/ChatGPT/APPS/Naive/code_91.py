def max_removable_length(s, t):
    n, m = len(s), len(t)
    
    # Create arrays to store the positions of t in s
    left = [0] * m
    right = [0] * m
    
    # Fill left array
    j = 0
    for i in range(n):
        if j < m and s[i] == t[j]:
            left[j] = i
            j += 1
    
    # Fill right array
    j = m - 1
    for i in range(n - 1, -1, -1):
        if j >= 0 and s[i] == t[j]:
            right[j] = i
            j -= 1
    
    # Calculate the maximum removable length
    max_length = 0
    for i in range(m - 1):
        max_length = max(max_length, right[i + 1] - left[i] - 1)
    
    # Check the edges
    max_length = max(max_length, right[0])  # Remove from start to first character of t
    max_length = max(max_length, n - 1 - left[m - 1])  # Remove from last character of t to end
    
    return max_length

# Input reading
s = input().strip()
t = input().strip()

# Output the result
print(max_removable_length(s, t))