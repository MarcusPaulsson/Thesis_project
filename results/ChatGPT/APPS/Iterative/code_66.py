def minimum_length_string(n, k, t):
    # Find the longest suffix of `t` that is also a prefix
    overlap_length = 0
    for i in range(1, n):
        if t.startswith(t[i:]):
            overlap_length = n - i
            break
    
    # Construct the result string
    result = t + (t[overlap_length:] * (k - 1))
    return result

# Input reading
n, k = map(int, input().split())
t = input().strip()

# Output the result
print(minimum_length_string(n, k, t))