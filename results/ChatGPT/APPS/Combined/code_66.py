def construct_string(n, k, t):
    # Compute the longest prefix which is also a suffix (LPS array)
    lps = [0] * n
    j = 0  # Length of the previous longest prefix suffix
    for i in range(1, n):
        while j > 0 and t[i] != t[j]:
            j = lps[j - 1]
        if t[i] == t[j]:
            j += 1
            lps[i] = j
        else:
            lps[i] = 0

    # Determine the length of the overlap
    overlap_length = lps[-1]
    
    # Construct the result string
    result = t + t[overlap_length:] * (k - 1)
    
    return result

# Input reading
n, k = map(int, input().split())
t = input().strip()

# Generate and print the result string
result_string = construct_string(n, k, t)
print(result_string)