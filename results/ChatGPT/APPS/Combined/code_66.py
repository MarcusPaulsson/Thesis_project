def minimum_length_string(n, k, t):
    # Step 1: Find the maximum overlap length
    overlap_length = 0
    for i in range(1, n):
        if t.startswith(t[i:]):
            overlap_length = n - i
            break

    # Step 2: Construct the result string
    # Start with the first occurrence of t
    result = t
    # Add remaining k-1 occurrences with the overlap
    result += t[overlap_length:] * (k - 1)

    return result

# Input reading
n, k = map(int, input().split())
t = input().strip()

# Output the result
print(minimum_length_string(n, k, t))