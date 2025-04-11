def max_removable_length(s, t):
    n, m = len(s), len(t)

    # Create arrays to store the first occurrence of t in s from the left and right
    left = [0] * m
    right = [0] * m

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

    # Calculate the maximum removable length
    max_length = 0
    for i in range(m - 1):
        max_length = max(max_length, right[i + 1] - left[i] - 1)

    # Check the case where we can remove from the start to the first character of t
    max_length = max(max_length, left[0])
    # Check the case where we can remove from the last character of t to the end
    max_length = max(max_length, n - 1 - right[m - 1])

    return max_length

# Input reading
s = input().strip()
t = input().strip()

# Output the result
print(max_removable_length(s, t))