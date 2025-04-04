def construct_string(n, k, t):
    # Find the longest suffix of t that is also a prefix
    for i in range(1, n):
        if t[:i] == t[-i:]:
            overlap_length = i
            break
    else:
        overlap_length = 0
    
    # Create the resulting string by using the prefix and overlap
    result = t + (t[overlap_length:] * (k - 1))
    
    return result

# Input reading
n, k = map(int, input().split())
t = input().strip()

# Construct and print the result
result = construct_string(n, k, t)
print(result)