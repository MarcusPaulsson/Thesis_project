def construct_string(n, k, t):
    # Find the longest prefix that is also a suffix
    prefix_suffix_length = 0
    for i in range(1, n):
        if t[:i] == t[-i:]:
            prefix_suffix_length = i
    
    # Construct the result string
    result = t + (t[prefix_suffix_length:] * (k - 1))
    
    return result

# Input reading
n, k = map(int, input().split())
t = input().strip()

# Output the result
print(construct_string(n, k, t))