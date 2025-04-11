def construct_string(n, k, t):
    # Find the longest prefix which is also a suffix
    lps = [0] * n
    j = 0  # length of previous longest prefix suffix
    i = 1

    while i < n:
        if t[i] == t[j]:
            j += 1
            lps[i] = j
            i += 1
        else:
            if j != 0:
                j = lps[j - 1]
            else:
                lps[i] = 0
                i += 1

    # The length of the longest prefix which is also a suffix
    longest_prefix_suffix = lps[-1]

    # The minimum length of the string s
    min_length = n + (k - 1) * (n - longest_prefix_suffix)

    # Construct the string s
    s = t
    for _ in range(k - 1):
        s += t[longest_prefix_suffix:]

    return s

# Read input
n, k = map(int, input().split())
t = input().strip()

# Get the result and print it
result = construct_string(n, k, t)
print(result)