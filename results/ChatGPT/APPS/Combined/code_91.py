def max_removable_length(s: str, t: str) -> int:
    n, m = len(s), len(t)
    
    # Initialize arrays to store the first and last occurrences of t's characters in s
    left, right = [-1] * m, [-1] * m

    # Fill the left array to find the first occurrences
    j = 0
    for i in range(n):
        if j < m and s[i] == t[j]:
            left[j] = i
            j += 1

    # Fill the right array to find the last occurrences
    j = m - 1
    for i in range(n - 1, -1, -1):
        if j >= 0 and s[i] == t[j]:
            right[j] = i
            j -= 1

    # Calculate the maximum removable length
    max_length = 0
    
    # Check removable length between the left and right occurrences
    for i in range(m - 1):
        max_length = max(max_length, right[i + 1] - left[i] - 1)

    # Consider removing characters before the first character of t
    max_length = max(max_length, left[0])
    # Consider removing characters after the last character of t
    max_length = max(max_length, n - right[m - 1] - 1)

    return max_length

# Input reading
s = input().strip()
t = input().strip()

# Output the result
print(max_removable_length(s, t))