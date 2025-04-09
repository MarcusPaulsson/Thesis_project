def minimum_length_string(n, k, t):
    # Find the longest prefix which is also a suffix
    for length in range(n-1, 0, -1):
        if t[:length] == t[-length:]:
            overlap_length = length
            break
    else:
        overlap_length = 0
    
    # Construct the result string
    result = t + (t[overlap_length:] * (k - 1))
    return result

# Input reading
n, k = map(int, input().split())
t = input().strip()

# Get the result and print it
result = minimum_length_string(n, k, t)
print(result)