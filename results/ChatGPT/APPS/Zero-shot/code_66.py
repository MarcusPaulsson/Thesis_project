def minimum_length_string(n, k, t):
    # Find the longest suffix of t that is also a prefix
    for i in range(n - 1, -1, -1):
        if t.startswith(t[i:]):
            overlap_length = i
            break
    
    # The length of the string s will be the length of t plus (k - 1) times the overlap length
    overlap = t[overlap_length:]
    s = t + overlap * (k - 1)
    
    return s

# Input reading
n, k = map(int, input().split())
t = input().strip()

# Output the result
print(minimum_length_string(n, k, t))