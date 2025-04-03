def construct_string(n, k, t):
    # Find the longest suffix of t that is also a prefix
    longest_suffix_prefix = 0
    for i in range(1, n):
        if t[:i] == t[-i:]:
            longest_suffix_prefix = i
            
    # Create the result string
    result = t + (t[longest_suffix_prefix:] * (k - 1))
    return result

# Input reading
n, k = map(int, input().split())
t = input().strip()

# Construct and print the result
print(construct_string(n, k, t))