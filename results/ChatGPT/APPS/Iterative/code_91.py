def max_removable_length(s, t):
    n, m = len(s), len(t)
    
    # Create arrays to store the position of match for t in s
    left = [-1] * m
    right = [-1] * m
    
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
    
    # Calculate the maximum removable substring length
    max_length = 0
    
    for i in range(m - 1):
        if left[i] != -1 and right[i + 1] != -1:
            max_length = max(max_length, right[i + 1] - left[i] - 1)
    
    # Also consider removing from the start or the end
    max_length = max(max_length, right[0] + 1)  # remove from the start
    max_length = max(max_length, n - left[m - 1] - 1)  # remove from the end
    
    return max_length

# Input reading
s = input().strip()
t = input().strip()

# Output the result
print(max_removable_length(s, t))