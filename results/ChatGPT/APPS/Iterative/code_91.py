def max_removable_length(s, t):
    n, m = len(s), len(t)
    
    # Precompute the leftmost positions of t in s
    left = [-1] * m
    j = 0
    for i in range(n):
        if j < m and s[i] == t[j]:
            left[j] = i
            j += 1
    
    # Precompute the rightmost positions of t in s
    right = [-1] * m
    j = m - 1
    for i in range(n - 1, -1, -1):
        if j >= 0 and s[i] == t[j]:
            right[j] = i
            j -= 1
    
    # Calculate the maximum removable length
    max_length = 0
    for i in range(m - 1):
        max_length = max(max_length, right[i + 1] - left[i] - 1)
    
    # Consider removing from the start to the first character of t
    max_length = max(max_length, right[0] + 1)
    # Consider removing from the last character of t to the end
    max_length = max(max_length, n - left[m - 1] - 1)
    
    return max_length

s = input().strip()
t = input().strip()
print(max_removable_length(s, t))