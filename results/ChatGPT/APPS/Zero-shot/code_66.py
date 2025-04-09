def minimum_length_string(n, k, t):
    # Find the longest prefix which is also a suffix
    # This is used to minimize overlaps
    lps = [0] * n
    j = 0
    
    # Preprocess the pattern to create the lps array
    for i in range(1, n):
        while (j > 0 and t[i] != t[j]):
            j = lps[j - 1]
        if t[i] == t[j]:
            j += 1
            lps[i] = j
        else:
            lps[i] = 0

    # Length of the longest prefix which is also a suffix
    overlap_length = lps[-1]
    
    # Calculate the minimum length of the resultant string
    # Start with the first occurrence of t
    result = t
    
    # Add (k-1) occurrences of the remaining part of t after the overlap
    result += (t[overlap_length:] * (k - 1))
    
    return result

# Read input
n, k = map(int, input().split())
t = input().strip()

# Get the result
result = minimum_length_string(n, k, t)

# Print the result
print(result)