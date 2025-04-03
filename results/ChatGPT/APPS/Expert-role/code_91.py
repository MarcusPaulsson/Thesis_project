def max_remove_length(s, t):
    n, m = len(s), len(t)
    
    # Precompute the indices of t in s from the left
    left = [-1] * m
    j = 0
    for i in range(n):
        if j < m and s[i] == t[j]:
            left[j] = i
            j += 1
    
    # Precompute the indices of t in s from the right
    right = [-1] * m
    j = m - 1
    for i in range(n - 1, -1, -1):
        if j >= 0 and s[i] == t[j]:
            right[j] = i
            j -= 1
    
    # Calculate the maximum removable length
    max_removable = 0
    for i in range(m - 1):
        max_removable = max(max_removable, right[i + 1] - left[i] - 1)
    
    return max_removable

# Read input
s = input().strip()
t = input().strip()

# Get the result and print it
print(max_remove_length(s, t))