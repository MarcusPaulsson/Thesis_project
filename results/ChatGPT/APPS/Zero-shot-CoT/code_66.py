def construct_string(n, k, t):
    # Find the longest prefix which is also a suffix
    lps = [0] * n
    j = 0  # length of previous longest prefix suffix
    i = 1

    # Preprocess the pattern to create the lps array
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

    # Construct the result string
    # Start with the first occurrence of t
    result = t

    # Append (k-1) times the remaining part of t after the longest prefix suffix
    result += t[longest_prefix_suffix:] * (k - 1)

    return result

# Read input
n, k = map(int, input().split())
t = input().strip()

# Get the result and print it
result = construct_string(n, k, t)
print(result)