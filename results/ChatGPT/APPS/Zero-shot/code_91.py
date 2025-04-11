def max_removable_length(s, t):
    n, m = len(s), len(t)
    
    # Precompute the leftmost indices where t can be matched in s
    left = [0] * m
    j = 0
    for i in range(n):
        if j < m and s[i] == t[j]:
            left[j] = i
            j += 1
    
    # Precompute the rightmost indices where t can be matched in s
    right = [0] * m
    j = m - 1
    for i in range(n - 1, -1, -1):
        if j >= 0 and s[i] == t[j]:
            right[j] = i
            j -= 1
    
    # Now find the maximum removable length
    max_length = 0
    for i in range(m - 1):
        max_length = max(max_length, right[i + 1] - left[i] - 1)
    
    # Consider removing from the start to the first character of t
    max_length = max(max_length, right[0])
    # Consider removing from the last character of t to the end
    max_length = max(max_length, n - 1 - left[m - 1])
    
    return max_length

# Input reading
s = input().strip()
t = input().strip()

# Output the result
print(max_removable_length(s, t))