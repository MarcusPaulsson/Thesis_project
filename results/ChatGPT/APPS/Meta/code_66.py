def construct_string(n, k, t):
    # Find the longest prefix which is also a suffix
    # This helps in determining the overlap
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

    # Length of the overlap
    overlap_length = lps[-1]
    
    # The minimum length of the string s
    # The first occurrence of t is fully included, then we add (k-1) * (n - overlap_length)
    result_length = n + (k - 1) * (n - overlap_length)
    
    # Construct the result string
    result = t  # start with the first occurrence
    for _ in range(1, k):
        result += t[overlap_length:]  # add the non-overlapping part

    return result

# Input reading
n, k = map(int, input().split())
t = input().strip()

# Output the result
print(construct_string(n, k, t))