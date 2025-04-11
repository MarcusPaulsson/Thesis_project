def construct_string(n, k, t):
    # Find the longest suffix of t which is also a prefix
    overlap_length = 0
    for i in range(1, n):
        if t.startswith(t[i:]):
            overlap_length = n - i
            break

    # Construct the result string
    result = t + (t[overlap_length:] * (k - 1))
    return result

# Read input
n, k = map(int, input().split())
t = input().strip()

# Get the result and print it
result_string = construct_string(n, k, t)
print(result_string)