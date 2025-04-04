def max_removable_length(s, t):
    n, m = len(s), len(t)

    # Early exit if t is longer than s
    if m > n:
        return n

    # Create an array to store the position of each character of t in s
    pos_t = []
    j = 0
    for i in range(n):
        if j < m and s[i] == t[j]:
            pos_t.append(i)
            j += 1

    # If not all characters of t are found in s, return the full length of s
    if len(pos_t) < m:
        return n

    # Leftmost and rightmost indices to keep t as a subsequence
    left, right = pos_t[0], pos_t[-1]

    # The maximum removable length is the total length minus the length of remaining parts
    max_removal_length = left + (n - right - 1)

    return max_removal_length

# Input reading
s = input().strip()
t = input().strip()

# Output the result
print(max_removable_length(s, t))