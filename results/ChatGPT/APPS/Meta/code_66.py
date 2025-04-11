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
    overlap_length = lps[-1]

    # Construct the result string
    result = t
    for _ in range(k - 1):
        result += t[overlap_length:]  # Append the non-overlapping part

    return result

# Input reading
n, k = map(int, input().split())
t = input().strip()

# Get the result and print it
result = construct_string(n, k, t)
print(result)