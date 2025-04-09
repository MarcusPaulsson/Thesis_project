def max_removable_length(s, t):
    n = len(s)
    m = len(t)

    # Arrays to store the positions of characters in s that match t
    left = [0] * m
    right = [0] * m

    # Find the first occurrence of each character of t in s from left to right
    j = 0
    for i in range(n):
        if j < m and s[i] == t[j]:
            left[j] = i
            j += 1

    # Find the first occurrence of each character of t in s from right to left
    j = m - 1
    for i in range(n - 1, -1, -1):
        if j >= 0 and s[i] == t[j]:
            right[j] = i
            j -= 1

    # Calculate the maximum removable length
    max_length = 0
    for i in range(m - 1):
        max_length = max(max_length, right[i + 1] - left[i] - 1)

    # Check the lengths for removing from the start and end
    max_length = max(max_length, right[0])  # Remove from start
    max_length = max(max_length, n - 1 - left[m - 1])  # Remove from end

    return max_length

# Input reading
s = input().strip()
t = input().strip()

# Output the result
print(max_removable_length(s, t))