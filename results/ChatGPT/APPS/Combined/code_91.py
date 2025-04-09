def max_removable_substring_length(s: str, t: str) -> int:
    n, m = len(s), len(t)
    
    # Precompute leftmost indices of each character in t from s
    left_indices = [-1] * m
    j = 0
    for i in range(n):
        if j < m and s[i] == t[j]:
            left_indices[j] = i
            j += 1
    
    # Precompute rightmost indices of each character in t from s
    right_indices = [-1] * m
    j = m - 1
    for i in range(n - 1, -1, -1):
        if j >= 0 and s[i] == t[j]:
            right_indices[j] = i
            j -= 1

    # Calculate maximum removable length
    max_removable_length = 0
    for i in range(m - 1):
        max_removable_length = max(max_removable_length, right_indices[i + 1] - left_indices[i] - 1)

    # Consider removing from the start or the end of the string
    max_removable_length = max(max_removable_length, left_indices[0])  # Removing from start
    max_removable_length = max(max_removable_length, n - 1 - right_indices[m - 1])  # Removing from end

    return max_removable_length

# Input reading
if __name__ == "__main__":
    s = input().strip()
    t = input().strip()
    
    # Output the result
    print(max_removable_substring_length(s, t))