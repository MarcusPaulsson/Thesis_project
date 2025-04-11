def construct_string(n, k, t):
    # Find the longest suffix of t that is also a prefix
    longest_overlap = 0
    for i in range(1, n):
        if t[:n - i] == t[i:]:
            longest_overlap = n - i
            break
            
    # Construct the result string
    result = t + (t[longest_overlap:] * (k - 1))
    return result

# Read input
n, k = map(int, input().split())
t = input().strip()

# Get the result and print it
result = construct_string(n, k, t)
print(result)