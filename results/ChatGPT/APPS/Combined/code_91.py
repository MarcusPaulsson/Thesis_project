def max_removable_length(s: str, t: str) -> int:
    n, m = len(s), len(t)

    # Create arrays to store the first occurrence of t in s from the left and right
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

    # Calculate the maximum removable length
    max_length = 0
    for i in range(m - 1):
        max_length = max(max_length, right[i + 1] - left[i] - 1)

    # Check the case where we can remove from the start to the end of t
    max_length = max(max_length, left[m - 1])

    # Check the case where we can remove from the start of t to the end of s
    max_length = max(max_length, n - right[0] - 1)

    return max_length