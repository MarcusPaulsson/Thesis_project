def minimum_string(n, k, t):
    # Find the longest suffix of t that is also a prefix
    # This will help in minimizing the length of the resulting string
    longest_overlap = 0
    for i in range(1, n):
        if t[:n - i] == t[i:]:
            longest_overlap = n - i
            break
    
    # Construct the result
    result = t + (t[longest_overlap:] * (k - 1))
    return result

# Input reading
n, k = map(int, input().split())
t = input().strip()

# Get the minimum string
result = minimum_string(n, k, t)

# Output the result
print(result)