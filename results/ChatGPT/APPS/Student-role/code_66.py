def minimum_length_string(n, k, t):
    # Find the longest prefix which is also a suffix
    lps = [0] * n
    j = 0
    for i in range(1, n):
        while j > 0 and t[i] != t[j]:
            j = lps[j - 1]
        if t[i] == t[j]:
            j += 1
            lps[i] = j
        else:
            lps[i] = 0

    # The length of the overlap
    overlap = lps[-1]
    
    # Construct the result
    result = t + t[overlap:] * (k - 1)
    return result

# Read input
n, k = map(int, input().split())
t = input().strip()

# Get the result and print it
result = minimum_length_string(n, k, t)
print(result)