def construct_string(n, k, t):
    # Find the longest suffix of t that is also a prefix
    for i in range(n - 1, -1, -1):
        if t[:i] == t[-i:]:
            overlap_length = i
            break
    else:
        overlap_length = 0

    # Construct the result string
    result = t + (t[overlap_length:] * (k - 1))
    return result

# Read input
n, k = map(int, input().split())
t = input().strip()

# Get the result and print it
result = construct_string(n, k, t)
print(result)