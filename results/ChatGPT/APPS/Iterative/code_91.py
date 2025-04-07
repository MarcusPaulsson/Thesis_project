def max_removable_length(s, t):
    n, m = len(s), len(t)
    
    # Find the first occurrences of t in s
    left = [0] * m
    j = 0
    for i in range(n):
        if j < m and s[i] == t[j]:
            left[j] = i
            j += 1
    
    # Find the last occurrences of t in s
    right = [0] * m
    j = m - 1
    for i in range(n - 1, -1, -1):
        if j >= 0 and s[i] == t[j]:
            right[j] = i
            j -= 1
    
    max_length = 0
    
    # Calculate the maximum removable length
    for i in range(m - 1):
        max_length = max(max_length, right[i + 1] - left[i] - 1)
    
    # Consider removing from the start to the first occurrence of t[0]
    max_length = max(max_length, left[0])
    
    # Consider removing from the last occurrence of t[m-1] to the end
    max_length = max(max_length, n - right[m - 1] - 1)
    
    return max_length

# Input
s = input().strip()
t = input().strip()

# Output
print(max_removable_length(s, t))