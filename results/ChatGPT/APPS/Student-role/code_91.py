def max_removable_length(s, t):
    n, m = len(s), len(t)
    
    # Create arrays to store the first position of each character in t
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

    max_length = 0

    for i in range(m - 1):
        max_length = max(max_length, right[i + 1] - left[i] - 1)

    max_length = max(max_length, right[0] + (n - left[m - 1] - 1))

    return max_length

s = input().strip()
t = input().strip()
print(max_removable_length(s, t))