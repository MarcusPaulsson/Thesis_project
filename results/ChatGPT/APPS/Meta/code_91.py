def max_removable_length(s, t):
    n, m = len(s), len(t)
    
    # Create arrays to store the position of characters from 't' in 's'
    left = [-1] * m
    right = [-1] * m
    
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
    
    # Consider removing from the start or end
    max_length = max(max_length, right[0])  # Remove from start to the first occurrence of t[0]
    max_length = max(max_length, n - 1 - left[m - 1])  # Remove from the last occurrence of t[m-1] to the end
    
    return max_length

# Input reading
s = input().strip()
t = input().strip()

# Function call and output
print(max_removable_length(s, t))