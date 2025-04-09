def max_removable_length(s, t):
    n, m = len(s), len(t)

    # Precompute the leftmost positions of each character in t
    left = [0] * m
    j = 0
    for i in range(n):
        if j < m and s[i] == t[j]:
            left[j] = i
            j += 1

    # Precompute the rightmost positions of each character in t
    right = [0] * m
    j = m - 1
    for i in range(n - 1, -1, -1):
        if j >= 0 and s[i] == t[j]:
            right[j] = i
            j -= 1

    # Calculate the maximum removable length
    max_length = 0
    for i in range(m - 1):
        max_length = max(max_length, right[i + 1] - left[i] - 1)

    # Check for the case when we can remove from start to rightmost of t
    max_length = max(max_length, right[0] + 1)

    # Check for the case when we can remove from leftmost of t to end
    max_length = max(max_length, n - left[m - 1] - 1)

    return max_length

# Input reading
s = input().strip()
t = input().strip()

# Output the result
print(max_removable_length(s, t))