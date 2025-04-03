def construct_string(n, k, t):
    # Find the longest suffix of t that is also a prefix
    for i in range(n - 1, -1, -1):
        if t.startswith(t[i:]):
            overlap = i
            break
            
    # Construct the result string
    result = t + (t[overlap:] * (k - 1))
    return result

# Read input
n, k = map(int, input().split())
t = input().strip()

# Get the constructed string
result = construct_string(n, k, t)

# Print the result
print(result)