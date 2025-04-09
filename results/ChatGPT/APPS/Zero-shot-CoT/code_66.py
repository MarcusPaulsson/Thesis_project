def construct_string(n, k, t):
    # Find the longest prefix which is also a suffix
    lps = [0] * n
    j = 0
    for i in range(1, n):
        while (j > 0 and t[i] != t[j]):
            j = lps[j - 1]
        if t[i] == t[j]:
            j += 1
            lps[i] = j
        else:
            lps[i] = 0

    # Length of the overlap
    overlap_length = lps[-1]

    # Construct the result string
    result = t + (t[overlap_length:] * (k - 1))
    return result

# Input
n, k = map(int, input().split())
t = input().strip()

# Output
print(construct_string(n, k, t))