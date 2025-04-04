def max_removable_length(s: str, t: str) -> int:
    n, m = len(s), len(t)
    
    # Precompute the left and right indices of t in s
    left = [-1] * m
    right = [-1] * m
    
    j = 0
    for i in range(n):
        if j < m and s[i] == t[j]:
            left[j] = i
            j += 1
    
    j = m - 1
    for i in range(n - 1, -1, -1):
        if j >= 0 and s[i] == t[j]:
            right[j] = i
            j -= 1
    
    # Calculate maximum removable length
    max_length = 0
    for i in range(m - 1):
        max_length = max(max_length, right[i + 1] - left[i] - 1)
    
    # Check the case for removing from the start or the end
    max_length = max(max_length, right[0])  # Remove from start to right[0]
    max_length = max(max_length, n - left[m - 1] - 1)  # Remove from left[m-1] to end

    return max_length

# Input reading
s = input().strip()
t = input().strip()

# Output the result
print(max_removable_length(s, t))